# def palindromes(string: str):
#     first_half = string[0 : (len(string) // 2)]
#     if len(string) % 2 == 0:
#         second_half = string[(len(string) // 2) : ]
#     else:
#         second_half = string[(len(string) // 2) + 1 : ]
#     return first_half == second_half[::-1]


def palindromes(string: str):
    for i in range(len(string) // 2):
        if string[i] != string[len(string) - i - 1]:
            return False
    return True
            

while True:
    palindrome = input("Please type in a palindrome: ")
    if palindromes(palindrome):
        print(f"{palindrome} is a palindrome!")
        break
    
    print("that wasn't a palindrome")

