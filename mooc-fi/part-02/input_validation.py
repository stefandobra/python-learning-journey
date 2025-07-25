from math import sqrt

while True:
    number = int(input("Number? "))
    if number < 0:
        print("Invalid number")
    elif number > 0:
        print (sqrt(number))
    else:
        break
print("Exiting...")