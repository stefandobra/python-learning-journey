def most_common_character(string: str):
    most_common = string[0]
    for char in string:
        if string.count(char) > string.count(most_common):
            most_common = char

    
    return most_common

