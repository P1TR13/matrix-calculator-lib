import os
from matrix_lib import Matrix, SquareMatrix, IdentityMatrix, DiagonalMatrix, load_matrices_from_file
    

path = "./matrix.txt"
matrices = load_matrices_from_file(path)
print(f"Loaded {len(matrices)} matrices from {path}:\n")
for i, matrix in enumerate(matrices):
    print(f"Matrix {i + 1}:\n{matrix}\n")