import socket

UDP_IP = "192.168.1.2"
UDP_PORT = 5005

MESSAGE = "HELLO WORLD"

print("UDP target: " + UDP_IP)
print("UDP target port: " + str(UDP_PORT))
print("")

sock = socket.socket(socket.AF_INET,	# Internet
		    socket.SOCK_DGRAM)	# UDP
while True:
	sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
	MESSAGE = raw_input("Enter a message: ")
