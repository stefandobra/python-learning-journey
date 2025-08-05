def add(phonebook: dict):
    name = input("name: ")
    number = input("number: ")
    if name not in phonebook:
        phonebook[name] = []  
    phonebook[name].append(number)
    print("ok!")


def search(phonebook: dict):
    name = input("name: ")
    if name in phonebook:
        for number in phonebook[name]:
            print(number)
    else:
        print("no number")

def main():
    phonebook = {}
    while True:
        command = input("command (1 search, 2 add, 3 quit): ")

        if command == "3":
            print("quitting...")
            break
        elif command == "1":
            search(phonebook)
        elif command == "2":
            add(phonebook)
        else:
            print("please use only 1,2 or 3")


main()





