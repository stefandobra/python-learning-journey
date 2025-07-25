# def all_the_longest(list: list):
#     longest = ""
#     new_list = []

#     for string in list:
#         if len(string) > len(longest):
#             new_list.clear()
#             longest = string
#             new_list.append(string)
#         elif len(string) == len(longest):
#             new_list.append(string)
#     return new_list


def all_the_longest(list: list):
    
    new_list = []

    for string in list:
        if new_list == [] or len(string) > len(new_list[0]):
            new_list = [string]
        elif len(string) == len(new_list[0]):
            new_list.append(string)
    return new_list