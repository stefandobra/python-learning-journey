word = input("word: ")
char = input("character: ")

index = word.find(char)

if index != -1 and index < len(word) - 3:
    print(word[index:index+3])