from core.network import Network


def main():
    """A simple test to calculate the round trip time of
    packets

    This test was performed on:
    Results:

    :return: None
    """
    with open("config/network.conf", "r") as config_file:
        lines = config_file.readlines()
        config_dict = {}
        # Read the configuration file into config_dict
        for line in lines:
            if not line.startswith("#"):    # if the line is not a comment
                split = line.split(":")
                try:
                    config_dict.update({split[0]: split[1]})
                except IndexError:
                    pass
        try:
            ip = config_dict["ip"]
        except KeyError:
            config_file.close()
            return
        network = Network(ip, 10, 1024)
        while True:
            message = ""
            network.broadcast(message)


if __name__ == "__main__":
    main()
