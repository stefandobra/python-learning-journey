string = input("string: ")

vowels = "aeo"
n = 0

while n < len(vowels):
    if vowels[n] in string:
        print(f"{vowels[n]} found")
    else:
        print(f"{vowels[n]} not found")
    n += 1
