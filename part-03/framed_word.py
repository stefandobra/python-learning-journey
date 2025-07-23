string = input("string: ")

print("*" * 30)

spaces_beggining = (28 - len(string)) // 2
spaces_end = spaces_beggining

if len(string) % 2 != 0:
    spaces_end += 1

print(f"*{spaces_beggining * " "}{string}{spaces_end * " "}*")
print("*" * 30)




# print("*" * 30)
# if len(string) % 2 == 0:
#     print(f"*{((28 - len(string))//2) * " "}{string}{((28 - len(string))//2) * " "}*")
# else:
#     print(f"*{((28 - len(string))//2) * " "}{string}{(((28 - len(string))//2) + 1) * " "}*")
# print("*" * 30)