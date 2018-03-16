import socket
import multiprocessing
import os
import time
import signal

from contrib.incoming_message import IncomingMessage
from contrib.outgoing_message import OutgoingMessage
from helpers.helpers import get_config, get_ip


def main():
    """ A simple processing example that concurrently runs two delay timed
    loops that print out information about the process they're running on.
    Used to allow the network to listen while it sends out information.
    
    """
    processes = list()
    processes.append(multiprocessing.Process(name="thread1", target=target, args=(1, 2)))
    processes.append(multiprocessing.Process(name="thread2", target=target, args=(2, 3)))
    print("Parent process id: " + str(os.getpid()))
    for process in processes:
        process.start()


def target(num1, num2):
    """

    :param num1:
    :param num2:
    :return: none
    """
    for i in range(4):
        print("Executing target: " + str(num1) + " with process: " + str(os.getpid()) +
              "\nWhose parent process is: " + str(os.getppid()))
        time.sleep(num2)
    os.abort()


class Network:
    def __init__(self, max_packet_length, buffer_size):
        """

        :param max_packet_length:
        :param buffer_size:
        :return: None
        """
        config_dict = get_config("network.conf")
        self.signature = get_ip()
        if self.signature is None:
            raise RuntimeError("Could not get ip address")
        try:
            self.port = int(config_dict['port'])
        except KeyError:
            raise RuntimeError("Key 'port' not in config file")
        except ValueError:
            raise RuntimeError("'port' could not be read as an int")
        self.max_packet_length = max_packet_length

        self.unreads = []
        self.logged_messages = []
        self.buffer_size = buffer_size
        self.listening_process = None

        self.broadcast_socket = None
        self.listen_socket = None
        
    def start_listening(self, connection_type):
        """
        Command to start listening for incoming messages of a specified type
        :param connection_type: a constant that's specified in the constant library
            example:
                socket.SOCK_DGRAM   - specifies a udp socket
                socket.SOCK_STREAM  - specifies a tcp socket
        :return: None

        """
        if self.listen_socket is None:
            try:
                self.listen_socket = socket.socket(socket.AF_INET, connection_type)
                self.listen_socket.bind((self.signature, self.port))
                self.listening_process = multiprocessing.Process(
                    name="listening_process_"+str(self.signature)+"d", target=self.update_messages)
                self.listening_process.daemon = True
                self.listening_process.start()
            except RuntimeError:
                raise RuntimeError("Listening socket failed to open")
        
    def stop_listening(self):
        """
        Command to stop listening for incoming messages
        :return: None

        """
        # noinspection PyBroadException
        try:
            os.kill(self.listening_process.pid, signal.CTRL_C_EVENT)
        except Exception:
            os.kill(self.listening_process.pid, signal.SIGTERM)
        self.listen_socket = None

    def update_messages(self):
        while True:
            data, addr = self.listen_socket.recvfrom(self.max_packet_length)
            incoming_message = IncomingMessage(data)
            if self.signature != str(addr) and len(self.unreads) < self.buffer_size:    # if we have space and the
                                                                                        # message isn't from ourselves
                self.unreads.append(incoming_message)
        
    def broadcast(self, message):
        """Sends an outgoing message to the IP address 255.255.255.255
        :param message: The message that is being broadcasted
        :return: None

        """
        if self.broadcast_socket is None:
            self.broadcast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.broadcast_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        broadcast_addr = "255.255.255.255"
        outgoing_message = OutgoingMessage(broadcast_addr, self.signature, message)
        self.broadcast_socket.sendto(outgoing_message.content.encode('utf-8'),
                                     (broadcast_addr, self.port))

    def close_broadcast(self):
        """Stops broadcasting messages and closing the broadcasting socket
        :return: None

        """
        try:
            self.broadcast_socket.shutdown()                             # stops broadcasting
            self.broadcast_socket.close()                                # closes the broadcasting socket
        except Exception:                                                # checks for an exception
            raise RuntimeWarning("Could not close broadcast_socket")
        self.broadcast_socket = None

    def read(self, num_msgs=1):
        """Return a list containing the first `num_msgs` messages from unreads
        and move them to `self.logged_messages` (moving the oldest messages out of
        logged_messages)
        :param num_msgs: an integer representing the number of messages to read
        :return: list<Message> containing the oldest unread messages, None if num_msgs is not an int

        """
        try:
            num_msgs = int(num_msgs)
        except ValueError:
            return None
        r = self.unreads[:num_msgs]                                 # Get num_msgs msgs from unreads
        self.unreads = self.unreads[len(r):]                        # Remove from unreads
        tmp = r[:]
        tmp.extend(self.logged_messages[:self.buffer_size-len(r)][:])
        self.logged_messages = tmp
        return r


if __name__ == "__main__":
    main()
