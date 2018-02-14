import datetime
import re


class Message:
    def __init__(self, addr_to, addr_from, content, timestamp=False, sign=False):
        self.addr_to = addr_to
        self.addr_from = addr_from
        self.content = content
        self.content += "<to>" + str(self.addr_to) + "</to>"
        self.content += "<from>" + str(self.addr_from) + "</from>"
        if timestamp:
            self.timestamp = datetime.datetime.now()
            self.timestamp_str = (str(self.timestamp.year)
                                  + "_" + str(self.timestamp.month)
                                  + "_" + str(self.timestamp.day)
                                  + "_" + str(self.timestamp.hour)
                                  + "_" + str(self.timestamp.minute)
                                  + "_" + str(self.timestamp.second))
            self.content += "<time_stamp>" + self.timestamp_str + "</time_stamp>"
        if sign:
            self.content += "<signature>" + str(self.addr_from) + "</signature>"

    def add_timestamp(self, content):
        pass

    def add_signature(self, content):
        pass

    def convert_to_message(self, xml_string):
        pass

    def find_values(self, key, attributes=None):
        #TODO find and return all of the values that match the given key and attributes
        #hint, use re
        pass

    def __str__(self):
        return self.content
