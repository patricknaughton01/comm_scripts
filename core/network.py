import socket
import threading
import time

def main():
    """ A simple threading example that starts two threads. Each
    uses a call to time.sleep for a different amount of time so
    that they print their output asynchronously.
    
    """
    """threads=[]
    threads.append(threading.Thread(name="thread1", target=target, args=(1, 2)))
    threads.append(threading.Thread(name="thread2", target=target, args=(2, 3)))
    for thread in threads:
        thread.start()
    pass
    
def target(num1, num2):
    for i in range(4):
        print("Executing target: " + str(num1) + " on thread: " + threading.currentThread().getName())
        time.sleep(num2)"""

class Network:
    def __init__(signature, max_packet_length):
        self.max_packet_length = max_packet_length
        
        
    def start_listening():
        pass
        
    def stop_listening():
        pass
        
    def broadcast():
        pass
        
if __name__ == "__main__":
    main()