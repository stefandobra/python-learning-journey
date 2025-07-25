def even_numbers(list: list):
    new_list =[]
    for number in list:
        if number % 2 == 0:
            new_list.append(number)
    return new_list