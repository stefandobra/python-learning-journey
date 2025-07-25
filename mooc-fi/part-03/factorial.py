while True:
    number = int(input("number: "))
    if number <= 0:
        break
    i = 1
    factorial = 1
    while i <= number:
        factorial *= i
        i += 1
    print(f"The factorial of the number {number} is {factorial}")


print("Thanks and bye!")
    