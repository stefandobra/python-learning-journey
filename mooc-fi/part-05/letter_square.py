# def create_letter_dcitionary(layers: int):
#     alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     letter_dictionary = {}
#     for i in range(1, layers + 1):
#         letter_dictionary[i] = alphabet[i-1]
#     return letter_dictionary

# def create_square(dictionary:dict, layers: int):
#   size = layers * 2 - 1
#   outer_char = dictionary[layers]

#   square = []

#   for i in range(size):
#     row = []
#     for j in range(size):
#       row.append(outer_char)
#     square.append(row)
  
#   return square

# def fill_square(dictionary:dict, square: list, layers: int):
  
#   size = layers * 2 - 1
  
#   for i in range(1, size - 1):
#     for j in range(1, size - 1):
#       distance = min(i, j, size - 1 - i, size - 1 - j)
#       square[i][j] = dictionary[layers - distance]        

#   return square


# layers = int(input("Layers: "))
# dictionary = create_letter_dcitionary(layers)
# square = create_square(dictionary, layers)
# fill_square(dictionary, square, layers)

# for row in square:
#   for char in row:
#     print(char, end="")
#   print()


layers = int(input("Layers: "))
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
left = ""
right = ""
index = layers - 1
size = layers * 2 - 1

while index >= 1:
  left = left + alphabet[index]
  right = alphabet[index] + right
  size -= 2
  print(f"{left}{alphabet[index] * size}{right}")
  index -= 1

while index <= layers - 1:
  print(f"{left}{alphabet[index] * size}{right}")
  left = left[:-1]
  right = right[1:]
  size += 2
  index += 1