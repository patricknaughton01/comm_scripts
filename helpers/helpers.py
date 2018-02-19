def remove_spaces(str):
    r = ""
    for i in range(len(str)):
        if not str[i].isspace():
            r += str[i]
    return r