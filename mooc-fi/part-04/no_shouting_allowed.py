def no_shouting(strings: list):
    new_list = []
    for string in strings:
        if not string.isupper():
            new_list.append(string)
    return new_list