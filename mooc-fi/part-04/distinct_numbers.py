def distinct_numbers(list: list):
    new_list = []
    for number in list:
        if number not in new_list:
            new_list.append(number)
            
    new_list = sorted(new_list)
    return(new_list)


def distinct_numbers(list: list):
    new_list = []
    for number in list:
        if number not in new_list:
            new_list.append(number)
            
    new_list.sort()
    return(new_list)


