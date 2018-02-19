import re

from helpers.helpers import get_attributes, find_last


def main():
    message = Message("<to attribute =' value' attribute2='v\\\'al' attribute3=\"why\">192.168.1.2</to>"
                      "<to attr =' value'>192.168.1.3</to>"
                      "<from>192.168.1.3</from>"
                      "<time_stamp>2018_2_18_0_0_0_0</time_stamp>")
    attr_example = message.find_values("to", {"attribute": "value", "attribute2": "v\\\'al", "attribute3": "why"})
    print("Searching with attributes: " + str(attr_example))
    search_example = message.find_values("to")
    print("Searching without attributes: " + str(search_example))


class Message:
    def __init__(self, content):
        self.content = content

    def find_values(self, key, attributes=None):
        if attributes is None:
            values = re.findall(r"<" + key + ".*?>(.*?)</" + key + ">", self.content)
            return values
        else:
            values = []
            key_vals = re.findall(r"<" + key + "(.*?>.*?)</" + key + ">", self.content)
            for key_val in key_vals:
                keys_attributes = get_attributes(key_val)
                add_value = True
                for attr in attributes:
                    if attr not in keys_attributes or attributes[attr] != keys_attributes[attr]:
                        add_value = False
                if add_value:
                    ind = find_last(">", key_val)
                    if ind != -1:
                        values.append(key_val[ind+1:])
            return values

    def __str__(self):
        return self.content


if __name__ == "__main__":
    main()
