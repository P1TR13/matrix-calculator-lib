def matrix_add(matrix_a, matrix_b):
    rows = len(matrix_a)
    cols = len(matrix_b[0])
    return [[matrix_a[i][j] + matrix_b[i][j] for j in range(cols)] for i in range(rows)]

def matrix_sub(matrix_a, matrix_b):
    rows = len(matrix_a)
    cols = len(matrix_b[0])
    return [[matrix_a[i][j] - matrix_b[i][j] for j in range(cols)] for i in range(rows)]

def matrix_mul(matrix_a, matrix_b):
    rows_a, cols_a = len(matrix_a), len(matrix_a[0])
    rows_b, cols_b = len(matrix_b), len(matrix_b[0])
    result = [[0.0 for _ in range(rows_a)] for _ in range(cols_b)]
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
    return result

def scalar_mul(matrix, scalar):
    return [[value * scalar for value in row] for row in matrix]

def transposition(matrix):
    matrix_T = [[] for _ in range(len(matrix[0]))]
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix_T[j].append(matrix[i][j])

    return matrix_T

def determinant(matrix):
    size = len(matrix)
    if size == 1:
        return matrix[0][0]
    elif size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    elif size == 3:
        return (matrix[0][0] * matrix[1][1] * matrix[2][2] +
                matrix[0][1] * matrix[1][2] * matrix[2][0] +
                matrix[0][2] * matrix[1][0] * matrix[2][1] -
                matrix[0][2] * matrix[1][1] * matrix[2][0] -
                matrix[0][1] * matrix[1][0] * matrix[2][2] -
                matrix[0][0] * matrix[1][2] * matrix[2][1])
    else:
        det = 0.0
        for col in range(size):
            submatrix = [row[:col] + row[col+1:] for row in matrix[1:]]
            det += ((-1) ** col) * matrix[0][col] * determinant(submatrix)
        return det
