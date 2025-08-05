# def row_correct(sudoku: list, row_no: int):
#     ordered_row = sorted(sudoku[row_no])

#     for i in range(1,9):
#         if ordered_row[i-1] > 0 and ordered_row[i-1] == ordered_row[i]:
#             return False
        
#     return True

def row_correct(sudoku: list, row_no: int):
    numbers = []

    for number in sudoku[row_no]:
        if number > 0 and number in numbers:
            return False
        numbers.append(number)

    return True



