# def print_sudoku(sudoku: list):
#     for i in range(1, 10):
#         for j in range(1, 10):
#             if sudoku[i-1][j-1] == 0 and j % 3 == 0:
#                 print(f"_ ", end = " ")
#             elif sudoku[i-1][j-1] == 0:
#                 print("_", end = " ")
#             elif j % 3 == 0:
#                 print(f"{sudoku[i-1][j-1]} ", end = " ")
#             else:
#                 print(f"{sudoku[i-1][j-1]}", end = " ")
#         if i % 3 == 0:
#             print()  
#         print()

def print_sudoku(sudoku: list):
    row_number = 0
    for row in sudoku:
        column_number = 0
        for element in row:
            column_number += 1
            if element == 0:
                element = "_"
            row_print = f"{element} "
            if column_number % 3 == 0 and column_number < 8:
                row_print += " "
            print(row_print, end="")
        print()
        row_number += 1
        if row_number % 3 == 0 and row_number < 8:
            print()

def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    sudoku[row_no][column_no] = number


if __name__ == "__main__":
    sudoku  = [
    [ 9, 0, 0, 0, 8, 0, 3, 0, 0 ],
    [ 2, 0, 0, 2, 5, 0, 7, 0, 0 ],
    [ 0, 2, 0, 3, 0, 0, 0, 0, 4 ],
    [ 2, 9, 4, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 7, 3, 0, 5, 6, 0 ],
    [ 7, 0, 5, 0, 6, 0, 4, 0, 0 ],
    [ 0, 0, 7, 8, 0, 3, 9, 0, 0 ],
    [ 0, 0, 1, 0, 0, 0, 0, 0, 3 ],
    [ 3, 0, 0, 0, 0, 0, 0, 0, 2 ],
    ]
    print_sudoku(sudoku)