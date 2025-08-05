# def column_correct(sudoku: list, column_no: int):
#     numbers = []

#     for i in range(len(sudoku)):
#         if sudoku[i][column_no] > 0 and sudoku[i][column_no] in numbers:
#             return False
#         numbers.append(sudoku[i][column_no])

#     return True

def column_correct(sudoku: list, column_no: int):
    numbers = []

    for row in sudoku:
        number = row[column_no]
        if number > 0  and number in numbers:
            return False
        numbers.append(number)

    return True
