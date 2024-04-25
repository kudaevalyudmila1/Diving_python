"""
Напишите функцию для транспонирования матрицы.
"""

def transpose_matrix(matrix): 
    """Функция для транспонирования матрицы."""

    new_matrix = [[0 for i in range(len(matrix))] for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            new_matrix[j][i] = matrix[i][j]
    return new_matrix        


matr = [[7, 9, 2], [1, 4, 5], [3, 5, 8]]
transpose_matrix(matr)
print(transpose_matrix(matr))