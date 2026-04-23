from matrix_lib import Matrix

print_matrix_info = lambda matrix: (print(matrix), print())

def test_add():
    m1 = Matrix(2, 2, [[1, 2], [3, 4]])
    m2 = Matrix(2, 2, [[5, 6], [7, 8]])

    print_matrix_info(m2 * 3)
    print_matrix_info(3 * m2)
    print_matrix_info(m1 + m2)
    print_matrix_info(m1 - m2)
    print_matrix_info(m2 - m1)
    print_matrix_info(m1 * m2)
    print_matrix_info(m1 + 'a')
    print_matrix_info(m1 + m2 + m1)
    

if __name__ == "__main__":
    test_add()
