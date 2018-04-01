import serial
import time


def main():
    ser = serial.Serial(
        port='/dev/ttyACM0',
        baudrate=9600,
    )
    while True:
        ser.write('e'.encode('utf-8'))
        ser.write('n1600l'.encode('utf-8'))
        time.sleep(2)
        ser.write('n1400l'.encode('utf-8'))
        time.sleep(2)


if __name__ == "__main__":
    main()
