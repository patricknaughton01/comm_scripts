import socket
import multiprocessing, os
import time


def main():
    """ A simple processing example that concurrently runs two delay timed
    loops that print out information about the process they're running on.
    Used to allow the network to listen while it sends out information.
    
    """
    processes=[]
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
            # TODO: create Message wrapper class from data and append to unreads if there's space for it
        
    def broadcast(self, message):
        #TODO: broadcast the passed message to the address 255.255.255.255
        pass

    def close_broadcast(self):
        #TODO: close self.broadcast_socket
        pass
        

if __name__ == "__main__":
    main()