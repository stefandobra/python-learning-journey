# def first_word(string):
#     space = string.find(" ")
#     return string[0:space]

# def second_word(string):
#     first_space = string.find(" ")
#     string = string[first_space + 1:]
#     space = string.find(" ")
#     if space > 0:
#         return string[0:space]
#     else:
#         return string
    


# def last_word(string):
#     while len(string) > 0:
        
#         space = string.find(" ")
#         if space > 0:
#             string = string[space + 1:]
#         else:
#             return string   

def find_word(string, position):
    word = ""
    index = 0
    counter = 0
    while index < len(string):
        if string[index] == " ":
            counter += 1
            if counter == position:
                break
            word =""
        else:
            word += string[index]
        index += 1
    return word

def first_word(string):
    return find_word(string, 1)

def second_word(string):
    return find_word(string, 2)

def last_word(string):
    return find_word(string, 0)



# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    #print(first_word(sentence))
    #print(second_word(sentence))
    print(last_word(sentence))