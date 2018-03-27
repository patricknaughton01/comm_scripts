import serial
import time


def main():
    ser = serial.Serial(
        port='',
        baudrate=9600,
        bytesize=serial.EIGHTBYTES,
        timeout=0.5,
    )
    while True:
        ser.write('s')
        ser.write(123)
        time.sleep(1)
        ser.write(0)


if __name__ == "__main__":
    main()