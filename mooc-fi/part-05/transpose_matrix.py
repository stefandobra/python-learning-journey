# def transpose(matrix: list):

#     new_matrix = []

#     for i in range(len(matrix)):
#         new_row = []
#         for row in matrix:
#             new_row.append(row[i])
#         new_matrix.append(new_row)

#     matrix[:] = new_matrix
        

def transpose(matrix: list):
    length = len(matrix)

    for i in range(length):
        for j in range(i, length):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp


            