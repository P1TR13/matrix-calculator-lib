from matrix_lib import Matrix, IdentityMatrix, SquareMatrix, DiagonalMatrix


def print_matrix_info(matrix):
    print(matrix)
    print()
    print(matrix.inverse())
    print("\n\n")

def test_inverse():
    m = Matrix(2, 2, [[1, 2], [3, 4]])
    m_i = IdentityMatrix(6)
    m_d = DiagonalMatrix(4, [3, 11, 90, -4])
    m_d2 = DiagonalMatrix(3, [[4, 0, 0], [0, -5, 0], [0, 0, 2.5]])
    m_s = SquareMatrix(3, [[5, 6, 7], [100, 20, 23], [-5, 0, 0]])
    m_5 = SquareMatrix(5, [[7, 0, 3, 1, 0], [2, 5, 0, 0, 4], [0, 8, 9, 2, 1], [6, 0, 4, 3, 0], [1, 3, 0, 7, 5]])

    print_matrix_info(m)
    print_matrix_info(m_i)
    print_matrix_info(m_d)
    print_matrix_info(m_d2)
    print_matrix_info(m_s)
    print_matrix_info(m_5)

if __name__ == "__main__":
    test_inverse()
