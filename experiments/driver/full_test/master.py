import serial

from core.network import Network


def main():
    ser = serial.Serial(
        port='/dev/ttyACM0',
        baudrate=9600,
        timeout=0,
    )
    network = Network(1024, 10)
    try:
        while True:
            command = ser.readline().decode('utf-8')
            network.broadcast("<command>" + command + "</command>")
    except KeyboardInterrupt:
        network.close_broadcast()


if __name__ == "__main__":
    main()