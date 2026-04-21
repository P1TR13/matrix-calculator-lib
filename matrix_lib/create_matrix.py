import matrix_lib.operations as operations
import matrix_lib.solving as solving


def safe_operation(func):
    """Dekorator obsługujący błędy w operatorach - zwraca None zamiast rzucić wyjątek"""
    def wrapper(self, other):
        try:
            return func(self, other)
        except (TypeError, ValueError) as e:
            print(f"Error in {func.__name__}: {e}")
            return None
    return wrapper


class Matrix:
    def __init__(self, rows=0, cols=0, data=None):
        self._rows = rows
        self._cols = cols
        self._data = data
        if data is not None:
            self.matrix = [[float(el) for el in row] for row in data]
        else:
            self.matrix = []

    @property
    def data_for_calc(self):
        return self.matrix

    def __str__(self):
        return "\n".join(" ".join(f"{el:6.2f}" for el in self.matrix[i]) for i in range(self._rows))
    
    @safe_operation
    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError(f"Can't add Matrix with {type(other).__name__}")
        result = operations.matrix_add(self.data_for_calc, other.data_for_calc)
        return Matrix(self._rows, self._cols, result)
    
    @safe_operation
    def __sub__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError(f"Can't subtract Matrix with {type(other).__name__}")
        result = operations.matrix_sub(self.data_for_calc, other.data_for_calc)
        return Matrix(self._rows, self._cols, result)
    
    @safe_operation
    def __mul__(self, other):
        if isinstance(other, Matrix):
            result = operations.matrix_mul(self.data_for_calc, other.data_for_calc)
            return Matrix(self._rows, other._cols, result)
        elif isinstance(other, (int, float)):
            result = operations.scalar_mul(self.data_for_calc, other)
            return Matrix(self._rows, self._cols, result)
        else:
            raise TypeError(f"Can't multiply Matrix by {type(other).__name__}")
        
    @safe_operation
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return False
        if self._rows != other._rows or self._cols != other._cols:
            return False
        epsilon = 1e-9
        for i in range(self._rows):
            for j in range(self._cols):
                if abs(self.matrix[i][j] - other.matrix[i][j]) > epsilon:
                    return False
        return True
    
    def transposition(self):
        return Matrix(self._rows, self._cols, operations.transposition(self.data_for_calc))
    
    def determinant(self):
        return None
    
    def inverse(self):
        return None
    
    def solve(self, b):
        return None
    

class SquareMatrix(Matrix):
    def __init__(self, size, data=None):
        super().__init__(size, size, data)

    def transposition(self):
        return SquareMatrix(self._rows, operations.transposition(self.data_for_calc))
    
    def determinant(self):
        return operations.determinant(self.data_for_calc)
    
    def inverse(self):
        if self.determinant() == 0:
            raise ValueError("Singular matrix — inverse does not exist")
        inv_data = operations.inverse(self.data_for_calc)
        return SquareMatrix(self._rows, inv_data)
    def solve(self, b):
        if self.determinant() == 0:
            raise ValueError("Singular matrix — can't solve")
        solving.Gauss(self.data_for_calc, b)
        return None


class DiagonalMatrix(SquareMatrix):
    def __init__(self, size, data=None):
        if data is None:
            diag = [0.0] * size
        elif isinstance(data[0], list):
            diag = [float(data[i][i]) for i in range(size)]
        else:
            diag = [float(x) for x in data]

        super().__init__(size, None)
        self.matrix = diag

    @property
    def data_for_calc(self):
        return [[self.matrix[i] if i == j else 0.0 for j in range(self._rows)] for i in range(self._rows)]

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
    
    def transposition(self):
        return DiagonalMatrix(self._rows, self.matrix)
    
    def determinant(self):
        det = 1.0
        for i in range(self._rows):
            det *= self.matrix[i]
        return det
    
    def inverse(self):
        if any(x == 0 for x in self.matrix):
            raise ValueError("Singular matrix — inverse does not exist")
        inv_diag = [1.0 / x for x in self.matrix]
        return DiagonalMatrix(self._rows, inv_diag)


class IdentityMatrix(DiagonalMatrix):
    def __init__(self, size):
        super().__init__(size, [1.0 for _ in range(size)])

    def transposition(self):
        return IdentityMatrix(self._rows)
    
    def determinant(self):
        return 1.0
    
    def inverse(self):
        return IdentityMatrix(self._rows)
