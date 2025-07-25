word = input("word: ")
char = input("character: ")

index = 0

while index + 3 <= len(word):
    if word[index] == char:
        print(word[index:index+3])
    index += 1