import time

from core.network import Network


def main():
    """A simple test to calculate the round trip time of
    packets

    This test was performed on:
    Results:

    :return: None
    """
    network = Network(10, 1024)
    while True:
        message = "<token>Token data</token>"               # send token data every 2 seconds
        network.broadcast(message)
        time.sleep(2)


if __name__ == "__main__":
    main()
