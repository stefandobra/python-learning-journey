def length_of_longest(list: list):
    longest = 0
    for string in list:
        if len(string) > longest:
            longest = len(string)
    return longest