import re

from helpers.helpers import remove_spaces


def main():
    message = Message("<to attribute =' value'>192.168.1.2</to>"
                      "<from>192.168.1.3</from>"
                      "<time_stamp>2018_2_18_0_0_0_0</time_stamp>")
    message.find_values("to", "attribute")


class Message:
    def __init__(self, content):
        self.content = content

    def find_values(self, key, attributes=None):
        if attributes is None:
            values = re.findall(r"<" + key + ">(.*?)</" + key + ">", self.content)
            return values
        else:
            potentials = {}
            key_vals = re.findall(r"<" + key + "(.*?>.*?)</" + key + ">", self.content)
            for i in range(len(key_vals)):
                key_vals[i] = remove_spaces(key_vals[i])
            print(key_vals)

    def __str__(self):
        return self.content


if __name__ == "__main__":
    main()
