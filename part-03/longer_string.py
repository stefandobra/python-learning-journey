string1 = input("string 1: ")
string2 = input("string 2: ")

if len(string1) == len(string2):
    print("The strings are equally long")
elif len(string1) > len(string2):
    print(f"{string1} is longer")
else:
    print(f"{string2} is longer")

