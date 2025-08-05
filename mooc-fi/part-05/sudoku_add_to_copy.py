# def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
#     copy_list = []
#     for row in sudoku:
#         copy_row = []
#         for element in row:
#             copy_row.append(element)
#         copy_list.append(copy_row)
#     copy_list[row_no][column_no] = number
#     return copy_list


def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    copy_list = []
    for row in sudoku:
        copy_list.append(row[:])

    copy_list[row_no][column_no] = number
    return copy_list
