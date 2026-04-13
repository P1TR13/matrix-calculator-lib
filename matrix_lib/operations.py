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