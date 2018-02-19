import datetime

from message import Message


def main():
    pass
    # TODO: write a test for this class


class OutgoingMessage(Message):
    def __init__(self, addr_to, addr_from, content, timestamp=True, sign=True):
        super(content)
        self.content += "<to>" + str(addr_to) + "</to>"
        if timestamp:
            self.add_timestamp()
        if sign:
            self.add_signature(addr_from)

    def add_timestamp(self):
        timestamp = datetime.datetime.now()
        timestamp_str = (str(timestamp.year)
                         + "_" + str(timestamp.month)
                         + "_" + str(timestamp.day)
                         + "_" + str(timestamp.hour)
                         + "_" + str(timestamp.minute)
                         + "_" + str(timestamp.second)
                         + "_" + str(timestamp.microsecond))
        self.content += "<time_stamp>" + timestamp_str + "</time_stamp>"

    def add_signature(self, signature):
        self.content += "<from>" + str(signature) + "</from>"


if __name__ == "__main__":
    main()
