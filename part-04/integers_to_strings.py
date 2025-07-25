def formatted(list: list):
    new_list = []
    for float in list:
        new_list.append(f"{float:.2f}")
    return new_list

