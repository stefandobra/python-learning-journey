word_1 = input("Please type in the 1st word: ")
word_2 = input("Please type in the 2st word: ")

if word_1 > word_2:
    print(f"{word_1} comes alphabetically last.")
elif word_2 > word_1:
    print(f"{word_2} comes alphabetically last.")
else:
    print("You gave the same word twice.")