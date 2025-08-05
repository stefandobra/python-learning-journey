# def dict_of_numbers():
#     numbers = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 
#                6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
#                11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
#                15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen",
#                19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty",
#                50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty",
#                90: "ninety", 0: "zero"
#                } 
#     new_dict = {}
    
#     for i in range (21, 100):
#         new_dict[i] = f"{numbers[(int(i/10)*10)]}-{numbers[i%10]}"
#     for key in numbers:
#         if key < 21 or key % 10 == 0:
#             new_dict[key] = numbers[key]

#     return(new_dict)

def dict_of_numbers():
    
    
    
    singles = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"} 
    tens = {20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}
    eleven_twenty = {10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 
                     16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}
    
    numbers = {}

    for key in singles:
        numbers[key] = singles[key]
    for key in eleven_twenty:
        numbers[key] = eleven_twenty[key]
    
    for i in range(2, 10):
        numbers[i * 10] = tens[i*10]
        for j in range(1,10):
            numbers[i * 10 + j] = f"{tens[i * 10]}-{singles[j]}"

    return numbers

if __name__ == "__main__":
    print(dict_of_numbers())