class Matrix:
    def __init__(self, rows, cols, data=None):
        self._rows = rows
        self._cols = cols
        self.matrix = data


class SquareMatrix(Matrix):
    def __init__(self, size, data=None):
        pass


class IdentityMatrix(SquareMatrix):
    pass


class DiagonalMatrix(SquareMatrix):
    pass
