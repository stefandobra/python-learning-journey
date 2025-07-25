def shortest(list: list):
    shortest = list[0]
    for string in list:
        if len(string) < len(shortest):
            shortest = string
    return shortest
