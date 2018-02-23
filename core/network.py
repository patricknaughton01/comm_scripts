import socket
import multiprocessing
import os
import time

from contrib.incoming_message import IncomingMessage
from contrib.outgoing_message import OutgoingMessage


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
    for i in range(4):
        print("Executing target: " + str(num1) + " with process: " + str(os.getpid()) +
              "\nWhose parent process is: " + str(os.getppid()))
        time.sleep(num2)
    os.abort()


class Network:
    def __init__(self, signature, max_packet_length, buffer_size):
        self.signature = signature
        self.max_packet_length = max_packet_length

        self.unreads = []
        self.logged_messages = []
        self.buffer_size = buffer_size
        self.listening_process = None

        self.broadcast_socket = None
        self.listen_socket = None
        
    def start_listening(self, ip, port, connection_type):
        if self.listen_socket is None:
            try:
                self.listen_socket = socket.socket(socket.AF_INET, connection_type)
                self.listen_socket.bind((ip, port))
                self.listening_process = multiprocessing.Process(
                    name="listening_process_"+str(self.signature), target=self.update_messages())
                self.listening_process.start()
            except RuntimeError:
                raise RuntimeError("Listening socket failed to open")
        
    def stop_listening(self):
        self.listening_process.abort()
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
        outgoing_message = OutgoingMessage("255.255.255.255", self.signature, message)
        self.broadcast_socket.sendto(outgoing_message.content, (outgoing_message.find_values("f")[0], 5005))

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
        r = self.unreads[:num_msgs]                             # Get num_msgs msgs from unreads
        self.unreads = self.unreads[len(r):]                    # Remove from unreads
        self.logged_messages = r.extend(
            self.logged_messages[:self.buffer_size-len(r)][:])  # Add to the logged_messages
        return r


if __name__ == "__main__":
    main()
