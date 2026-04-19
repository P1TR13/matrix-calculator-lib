from matrix_lib import Matrix, IdentityMatrix, SquareMatrix, DiagonalMatrix


def print_matrix_info(matrix):
    print(matrix)
    print()
    print(matrix.transposition())
    print()
    print(matrix.determinant())
    print("\n\n")

def test_t_and_det():
    m = Matrix(2, 2, [[1, 2], [3, 4]])
    m_i = IdentityMatrix(6)
    m_d = DiagonalMatrix(4, [3, 11, 90, -4])
    m_d2 = DiagonalMatrix(3, [[4, 0, 0], [0, -5, 0], [0, 0, 2.5]])
    m_s = SquareMatrix(3, [[5, 6, 7], [100, 20, 23], [-5, 0, 0]])

    print_matrix_info(m)
    print_matrix_info(m_i)
    print_matrix_info(m_d)
    print_matrix_info(m_d2)
    print_matrix_info(m_s)

if __name__ == "__main__":
    test_t_and_det()
