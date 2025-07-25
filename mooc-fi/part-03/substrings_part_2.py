string = input("string: ")

lenght = len(string) - 1

while lenght >= 0:
    print(string[lenght:])
    lenght -= 1