import serial
import socket

from core.network import Network


def main():
    ser = serial.Serial(
        port="/dev/ttyACM0",
        baudrate=9600,
        timeout=0,
    )
    network = Network(1024, 10)
    network.start_listening(socket.SOCK_DGRAM)
    try:
        while True:
            incoming_command = network.read().findValues("<command>")[0]
            if incoming_command.startswith("s"):
                ser.write(b's')
            elif incoming_command.startswith("e"):
                ser.write(b'e')
            ser.write(("n" + incoming_command[1:]).encode('utf-8'))
    except KeyboardInterrupt:
        network.stop_listening()


if __name__ == "__main__":
    main()