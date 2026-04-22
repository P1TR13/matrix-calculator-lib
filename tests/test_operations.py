from matrix_lib import Matrix


def test_add():
    m1 = Matrix(2, 2, [[1, 2], [3, 4]])
    m2 = Matrix(2, 2, [[5, 6], [7, 8]])
    print(m2 * 3)
    print()
    print(3 * m2)
    print()
    print(m1 + m2)
    print()
    print(m1 - m2)
    print()
    print(m2 - m1)
    print()
    print(m1 * m2)
    print()
    print(m1 + 'a')
    print()
    print(m1 + m2 + m1)
    

if __name__ == "__main__":
    test_add()
