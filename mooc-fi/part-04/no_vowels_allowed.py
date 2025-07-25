def no_vowels(string: str):
    vowels = "aeiou"
    new_string = ""
    for char in string:
        if char not in vowels:
            new_string += char
    return new_string