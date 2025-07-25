sentence = input("sentence: ")

print(sentence[0])

# while True:
#     if sentence.find(" ") != -1:
#         index = sentence.find(" ")
#         print(sentence[index+1])
#         sentence = sentence[index+1:]
#     else:    
#         break
i = 0

while i < len(sentence):
    if sentence[i] == " ":
        print(sentence[i+1])
    i += 1