import serial
import socket

from core.network import Network


def main():
    ser = serial.Serial(
        port="/dev/ttyACM0",
        baudrate=9600,
    )
    network = Network(1024, 10)
    network.start_listening(socket.SOCK_DGRAM)
    try:
        while True:
            incoming_command = network.read(network.buffer_size)
            if len(incoming_command) > 0:
                incoming_command = incoming_command[0].find_values("command")
                if len(incoming_command) > 0:
                    tmp = incoming_command.split(".")
                    esc = tmp[0].strip()
                    steer = tmp[1].strip()
                    ser.write(("e\n" + esc + "l\n").encode('utf-8'))
                    ser.write(("s\n" + steer + "l\n").encode('utf-8'))
    except KeyboardInterrupt:
        network.stop_listening()


if __name__ == "__main__":
    main()
