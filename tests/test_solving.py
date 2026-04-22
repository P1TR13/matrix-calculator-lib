from matrix_lib import SquareMatrix


def test_solving():
    A = SquareMatrix(3, [
        [1, 2, 3],
        [2, 3, 1],
        [3, 1, 2]
    ])

    b = [14, 11, 11]

    print(A.solve(b))

    A = SquareMatrix(4, [
        [4, 3, -2, 1],
        [2, -1, 5, -1],
        [1, 1, -1, 2],
        [-1, 2, 1, 1]
    ])

    b = [20, 15, 10, 8]

    print(A.solve(b))

    
if __name__ == "__main__":
    test_solving()