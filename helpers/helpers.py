def remove_spaces(str):
    r = ""
    for i in range(len(str)):
        if not str[i].isspace():
            r += str[i]
    return r


def get_attributes(str):
    str = remove_spaces(str)
    attr_vals = {}
    markers = []
    for i in range(len(str)):
        if str[i] == "'" or str[i] == '"':          # if we come upon a quote
            if i == 0 or str[i-1] != '\\':          # ignore the quote if it is escaped
                markers.append(i)
    if len(markers)%2 != 0:                         # must have an even number of quotes to be valid
        raise RuntimeError("get_attributes received a string whose quotes don't match up.")
    for i in range(0, len(markers)-1, 2):
        val = str[markers[i]+1:markers[i+1]]        # get string between the markers
        if i == 0:
            attr = str[:markers[i]-1]               # -1 to get rid of the equals sign (we know there won't be spaces)
        else:
            attr = str[markers[i-1]+1:markers[i]-1] # -1 to get rid of quote and equals sign
        attr_vals.update({attr:val})
    return attr_vals


def find_last(target, str):
    for i in range(len(str)-1, -1, -1):
        if str[i] == target:
            return i
    return -1