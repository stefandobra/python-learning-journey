# def double_items(numbers: list):
#     new_list = []
#     for number in numbers:
#         new_list.append(number * 2)

#     return new_list

def double_items(numbers: list):
    new_list = numbers[:]

    for i in range(len(new_list)):
        new_list[i] *= 2

    return new_list

if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)