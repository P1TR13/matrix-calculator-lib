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

    A = SquareMatrix(4, [
        [10, 1, 2, 3],
        [1, 8, 1, 2],
        [2, 1, 9, 1],
        [3, 2, 1, 11]
    ])
    b = [16, 12, 13, 17]
    print(A.solve(b))

    A = SquareMatrix(5, [
        [4, 3, -2, 1, 5],
        [2, -1, 5, -1, 3],
        [1, 1, -1, 2, 4],
        [-1, 2, 1, 1, -2],
        [3, 0, 2, -1, 6]
    ])
    b = [30, 20, 15, 10, 25]
    print(A.solve(b))

    A = SquareMatrix(10, [
        [10, 1, 2, 0, 1, 3, 1, 2, 0, 1],
        [1, 9, 0, 2, 1, 0, 2, 1, 3, 0],
        [2, 0, 8, 1, 2, 1, 0, 3, 1, 2],
        [0, 2, 1, 7, 0, 2, 1, 1, 2, 1],
        [1, 1, 2, 0, 6, 1, 2, 0, 1, 3],
        [3, 0, 1, 2, 1, 9, 0, 2, 1, 0],
        [1, 2, 0, 1, 2, 0, 8, 1, 2, 1],
        [2, 1, 3, 1, 0, 2, 1, 7, 0, 2],
        [0, 3, 1, 2, 1, 1, 2, 0, 9, 1],
        [1, 0, 2, 1, 3, 0, 1, 2, 1, 8]
    ])
    b = [25, 22, 20, 18, 24, 21, 19, 23, 26, 20]
    print(A.solve(b))

    # singular matrix
    A = SquareMatrix(3, [
        [1, 2, 3],
        [2, 4, 6],
        [3, 6, 9]
    ])
    b = [5, 10, 15]
    print(A.solve(b))

    # singular matrix
    A = SquareMatrix(3, [
        [1, 2, 3],
        [2, 4, 6],
        [3, 6, 9]
    ])
    b = [5, 10, 20]
    print(A.solve(b))

    # infinite solutions
    A = SquareMatrix(3, [
        [1, 2, 3],
        [2, 4, 6],      # Liniowo zależne
        [3, 6, 9]
    ])
    b = [5, 10, 15]
    print(A.solve(b))

    
if __name__ == "__main__":
    test_solving()