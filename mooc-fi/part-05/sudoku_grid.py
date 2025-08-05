def row_correct(sudoku: list, row_no: int):
    numbers = []

    for number in sudoku[row_no]:
        if number > 0 and number in numbers:
            return False
        numbers.append(number)

    return True


def column_correct(sudoku: list, column_no: int):
    numbers = []

    for row in sudoku:
        number = row[column_no]
        if number > 0  and number in numbers:
            return False
        numbers.append(number)

    return True

def block_correct(sudoku: list, row_no: int, column_no: int):
    numbers = []

    for i in range(row_no, row_no + 3):
        for j in range(column_no, column_no + 3):
            number = sudoku[i][j]
            if number > 0 and number in numbers:
                return False
            numbers.append(number)

    return True


def sudoku_grid_correct(sudoku: list):
        
    for row in range(0,9):
        if not row_correct(sudoku, row):
            return False    

    for column in range(0,9):
        if not column_correct(sudoku, column):
            return False
      
    for row in range(0, 9, 3):
        for column in range(0, 9, 3):
            if not block_correct(sudoku, row , column):
                return False
              
    return True
    
    
