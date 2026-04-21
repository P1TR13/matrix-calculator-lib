from matrix_lib import SquareMatrix


def test_solving():
    A = SquareMatrix(3, [
    [1, 2, 3],
    [2, 3, 1],
    [3, 1, 2]
    ])

    # Wektor b
    b = [14, 11, 11]

    A.solve(b)

    
if __name__ == "__main__":
    test_solving()