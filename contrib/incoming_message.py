from contrib.message import Message


def main():
    my_incoming_message = IncomingMessage("<to>192.168.1.2</to>"
                                          "<from>192.168.1.3</from>"
                                          "<time_stamp>2018_2_18_0_0_0_0</time_stamp>")
    print("Incoming message: " + str(my_incoming_message))
    print("Was broadcast: " + str(my_incoming_message.was_broadcast))

    my_incoming_message = IncomingMessage("<from>192.168.1.3</from>"
                                          "<time_stamp>2018_2_18_0_0_0_0</time_stamp>")
    print("Incoming message: " + str(my_incoming_message))
    print("Was broadcast: " + str(my_incoming_message.was_broadcast))

    my_incoming_message = IncomingMessage("<to>255.255.255.255</to>"
                                          "<from>192.168.1.3</from>"
                                          "<time_stamp>2018_2_18_0_0_0_0</time_stamp>")
    print("Incoming message: " + str(my_incoming_message))
    print("Was broadcast: " + str(my_incoming_message.was_broadcast))


class IncomingMessage(Message):
    def __init__(self, content):
        super().__init__(content)
        self.was_broadcast = self.was_broadcast()

    def was_broadcast(self):
        return len(self.find_values("to")) == 0 or self.find_values("to")[0][0:3] == "255"

    def directed_at_addr(self, addr):
        return self.find_values("to")[0] == addr


if __name__ == "__main__":
    main()
