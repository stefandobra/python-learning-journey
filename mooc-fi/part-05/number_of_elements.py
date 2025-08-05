def count_matching_elements(my_matrix: list, element: int):
    count = 0
    for row in my_matrix:
        for elem in row:
            if elem == element:
                count += 1
    return count

