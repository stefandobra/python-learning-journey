number = int(input("Please type in a number: "))

i = 1

while i <= number:
    if i == number:
        print(i)
        break
    print(f"{i+1}\n{i}")
    i += 2
    