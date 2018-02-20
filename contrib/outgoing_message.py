import datetime

from contrib.message import Message


def main():
    content = "<v>[10,10,0]</v><p>[10.3, 5, 0]</p>"
    outgoing_message = OutgoingMessage("255.255.255.255", "192.168.1.2", content)
    print("Outgoing message: " + str(outgoing_message))


class OutgoingMessage(Message):
    def __init__(self, addr_to, addr_from, content, timestamp=True, sign=True):
        super().__init__(content)
        self.content += "<t>" + str(addr_to) + "</t>"
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
        self.content += "<ts>" + timestamp_str + "</ts>"

    def add_signature(self, signature):
        self.content += "<f>" + str(signature) + "</f>"


if __name__ == "__main__":
    main()
