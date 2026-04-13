from . import operations

class Matrix:
    def __init__(self, rows, cols, data=None):
        self._rows = rows
        self._cols = cols
        self.matrix = data

    def __str__(self):
        return "\n".join(" ".join(f"{el:6.2f}" for el in self.matrix[i]) for i in range(self._rows))


class SquareMatrix(Matrix):
    def __init__(self, size, data=None):
        self._rows = size
        self.matrix = data


class DiagonalMatrix(SquareMatrix):
    def __init__(self, size, data=None):
        self._rows = size
        if data is None:
            self.matrix = [0.0] * size
        elif isinstance(data[0], list):
            self.matrix = [float(data[i][i]) for i in range(size)]
        else:
            self.matrix = [float(x) for x in data]

    def __str__(self):
        lines = []
        for i in range(self._rows):
            row = []
            for j in range(self._rows):
                if i == j:
                    row.append(f"{self.matrix[i]:6.2f}")
                else:
                    row.append(f"{0.0:6.2f}")
            lines.append("  ".join(row))
        return "\n".join(lines)


class IdentityMatrix(DiagonalMatrix):
    def __init__(self, size):
        self._rows = size
        self.matrix = [1.0 for _ in range(self._rows)]
