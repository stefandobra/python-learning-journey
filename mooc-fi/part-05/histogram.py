# def histogram(string: str):
#     histo = {}
#     for letter in string:
#         if letter not in histo:
#             histo[letter] = "*"
#         else:    
#             histo[letter] += "*"
    
#     for key, value in histo.items():
#         print(f"{key} {value}")

def histogram(string: str):
    histo = {}

    for char in string:
        if char not in histo:
            histo[char] = 0
        histo[char] += 1

    for char, count in histo.items():
        stars = "*" * count
        print(f"{char} {stars}")



    