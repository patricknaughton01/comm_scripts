import datetime

class Message:
    def __init__(addr_to, addr_from, content):
        self.addr_to = addr_to
        self.addr_from = addr_from
        self.content = content
        self.timestamp = datetime.datetime.now()
        self.timestamp_str = (str(self.timestamp.year)
                              + str(self.timestamp.month)
                              + str(self.timestamp.day)
                              + str(self.timestamp.hour)
                              + str(self.timestamp.minute)
                              + str(self.timestamp.second))
        self.content += "<signature>" + str(self.addr_from) + "</signature>"
        self.content += "<time_stamp>" + self.timestamp_str + "</time_stamp>"