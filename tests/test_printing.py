from matrix_lib import Matrix, SquareMatrix, DiagonalMatrix, IdentityMatrix


def test_add():
    m = Matrix(2, 2, [[1, 2], [3, 4]])
    m_i = IdentityMatrix(6)
    m_d = DiagonalMatrix(4, [3, 11, 90, -4])
    m_d2 = DiagonalMatrix(3, [[4, 0, 0], [0, -5, 0], [0, 0, 2.5]])
    m_s = SquareMatrix(3, [[5, 6, 7], [100, 20, 23], [-5, 0, 0]])

    print(m)
    print()
    print(m_i)
    print()
    print(m_d)
    print()
    print(m_d2)
    print()
    print(m_s)

if __name__ == "__main__":
    test_add()
