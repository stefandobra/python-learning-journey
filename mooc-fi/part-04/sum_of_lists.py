# def list_sum(a: list, b: list):
#     new_list = []
#     for i in range(len(a)):
#         new_list.append(a[i] + b[i])
#     return new_list


def list_sum(a: list, b: list):
    new_list = []
    for i, j in zip(a, b):
        new_list.append(i + j)    
    return new_list