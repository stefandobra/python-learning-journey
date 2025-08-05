# def remove_smallest(numbers: list):
#     sorted_list = sorted(numbers)
#     min = sorted_list[0]

#     index = numbers.index(min)
#     numbers.pop(index)


def remove_smallest(numbers: list):
    smallest = min(numbers)
    numbers.remove(smallest)

if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)