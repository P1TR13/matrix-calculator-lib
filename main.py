import os
from matrix_lib import Matrix, SquareMatrix, IdentityMatrix, DiagonalMatrix


def load_matrices_from_file(filepath):

    if not os.path.exists(filepath):
        print(f"Error: File {filepath} does not exist.")
        return []

    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read().strip()
        blocks = content.split('\n\n')

    matrices = []
    for block in blocks:
        try:
            lines = block.strip().split('\n')
            data = []

            expected_size = len(lines[0].split())

            for line in lines:
                row = [float(val) for val in line.split()]

                if len(row) != expected_size:
                    raise ValueError(f"wrong size of a matrix")

                data.append(row)

            if not data:
                continue

            print(data)
            matrices.append(identify_and_create_matrix(data))

        except ValueError as e:
            print(f"Error: {e}")

    return matrices

def identify_and_create_matrix(data):
    rows = len(data)
    cols = len(data[0])

    # if Square
    if rows != cols:
        return Matrix(rows, cols, data)
    
    # if Diagonal
    is_diagonal = True
    for r in rows:
        for c in cols:
            if r != c and data[r][c] != 0:
                is_diagonal = False
                break
        if not is_diagonal: break

    if is_diagonal:
        # if Identity
        is_identity = all(data[i][i] == 1.0 for i in range(rows))
        if is_identity:
            return IdentityMatrix(rows, data)
        return DiagonalMatrix(rows, data)
    
    return SquareMatrix(rows, data)
    

path = "./matrix.txt"
load_matrices_from_file(path)
