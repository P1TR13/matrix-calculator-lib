# Matrix Calculator Library

A comprehensive Python library for matrix operations and solving systems of linear equations using object-oriented principles.

## Features

- **Matrix Operations**: Addition, subtraction, multiplication (matrix-matrix, matrix-scalar), and transposition
- **Matrix Types**: Support for regular matrices, square matrices, diagonal matrices, and identity matrices
- **Determinant Calculation**: Efficient computation for 1×1, 2×2, 3×3, and n×n matrices
- **Matrix Inversion**: Calculate inverse matrices for non-singular systems
- **Linear Equation Solver**: Gaussian elimination with detection of singular matrices and inconsistent systems
- **File I/O**: Load matrices from text files with automatic type identification
- **Error Handling**: Graceful handling of edge cases (singular matrices, no solution, infinite solutions)

## Requirements

- Python 3.7 or higher
- No external dependencies

## Installation

Clone the repository:
```bash
git clone https://github.com/P1TR13/matrix-calculator-lib.git
cd matrix_calculator
```

## Usage

### Basic Matrix Operations

```python
from matrix_lib import Matrix, SquareMatrix

# Create matrices
M1 = Matrix(2, 2, [[1, 2], [3, 4]])
M2 = Matrix(2, 2, [[5, 6], [7, 8]])

# Addition
result = M1 + M2

# Subtraction
result = M1 - M2

# Scalar multiplication
result = M1 * 3

# Matrix multiplication
result = M1 * M2

# Transposition
result = M1.transposition()

# Print formatted output
print(M1)
```

### Square Matrices

```python
from matrix_lib import SquareMatrix

# Create a square matrix
A = SquareMatrix(3, [
    [1, 2, 3],
    [2, 3, 1],
    [3, 1, 2]
])

# Calculate determinant
det = A.determinant()
print(f"Determinant: {det}")

# Calculate inverse
A_inv = A.inverse()
print(A_inv)
```

### Solving Systems of Linear Equations

```python
from matrix_lib import SquareMatrix

# Define system Ax = b
A = SquareMatrix(3, [
    [4, 3, -2],
    [2, -1, 5],
    [1, 1, -1]
])

b = [20, 15, 10]

# Solve using Gaussian elimination
solution = A.solve(b)

if solution:
    print(f"Solution x = {[f'{x:.3f}' for x in solution]}")
else:
    print("System has no unique solution")
```

### Special Matrix Types

```python
from matrix_lib import DiagonalMatrix, IdentityMatrix

# Diagonal matrix
D = DiagonalMatrix(3, [2, 5, 3])
print(D)

# Identity matrix
I = IdentityMatrix(4)
print(I)
```

### Loading Matrices from File

```python
from matrix_lib import load_matrices_from_file

matrices = load_matrices_from_file("path/to/matrix.txt")
for matrix in matrices:
    print(matrix)
```

File format (space-separated, empty line between matrices):
```
1 2 3
4 5 6
7 8 9

1 0 0
0 1 0
0 0 1
```

## API Reference

### Matrix Class

**Constructor:**
- `Matrix(rows, cols, data=None)` - Create a matrix

**Methods:**
- `__add__(other)` - Matrix addition
- `__sub__(other)` - Matrix subtraction
- `__mul__(other)` - Matrix/scalar multiplication
- `transposition()` - Return transposed matrix
- `determinant()` - Returns None (override in subclasses)
- `inverse()` - Returns None (override in subclasses)
- `__str__()` - Formatted string representation

### SquareMatrix Class

Extends Matrix with:
- `determinant()` - Calculate determinant
- `inverse()` - Calculate inverse matrix
- `solve(b)` - Solve Ax = b system
  - Returns: `list` (solution), or `None` with error message if no unique solution

### DiagonalMatrix Class

Extends SquareMatrix for diagonal matrices:
- Optimized operations for diagonal storage
- Efficient determinant: product of diagonal elements
- Efficient inverse computation

### IdentityMatrix Class

Extends DiagonalMatrix:
- Identity matrix of given size
- Determinant always returns 1.0
- Inverse is itself

### Load Function

- `load_matrices_from_file(filepath)` - Load matrices from text file
  - Automatically identifies matrix type (regular, diagonal, identity, or square)

## Examples

### Example 1: Solve 3×3 System

```python
from matrix_lib import SquareMatrix

A = SquareMatrix(3, [
    [1, 2, 3],
    [2, 3, 1],
    [3, 1, 2]
])

b = [14, 11, 11]
solution = A.solve(b)
print([f"{x:.3f}" for x in solution])  # [1.000, 2.000, 3.000]
```

### Example 2: Handle Singular Matrix

```python
from matrix_lib import SquareMatrix

# Linearly dependent rows
A = SquareMatrix(3, [
    [1, 2, 3],
    [2, 4, 6],
    [3, 6, 9]
])

b = [5, 10, 20]
result = A.solve(b)  # Prints: No solution
```

### Example 3: Large System (5×5)

```python
from matrix_lib import SquareMatrix

A = SquareMatrix(5, [
    [4, 3, -2, 1, 5],
    [2, -1, 5, -1, 3],
    [1, 1, -1, 2, 4],
    [-1, 2, 1, 1, -2],
    [3, 0, 2, -1, 6]
])

b = [30, 20, 15, 10, 25]
solution = A.solve(b)
print([f"{x:.3f}" for x in solution])
```

## Running Tests

```bash
python -m tests.test_solving
python -m tests.test_inverse
python -m tests.test_operations
python -m tests.test_t_and_det
python -m tests.test_printing
```

## Project Structure

```
matrix_calculator/
├── matrix_lib/
│   ├── __init__.py           # Package initialization
│   ├── create_matrix.py      # Matrix class definitions
│   ├── load_matrix.py        # File loading utilities
│   ├── operations.py         # Matrix operations
│   └── solving.py            # Gaussian elimination solver
├── tests/
│   ├── test_solving.py       # System solving tests
│   ├── test_inverse.py       # Inverse matrix tests
│   ├── test_operations.py    # Basic operations tests
│   ├── test_t_and_det.py     # Transpose and determinant tests
│   └── test_printing.py      # Output formatting tests
├── main.py                   # Example usage
├── matrix.txt                # Sample matrix data
├── README.md                 # This file
└── LICENSE                   # MIT License
```

## Error Handling

The library handles the following cases gracefully:

1. **Singular Matrix** (det = 0):
   - Returns `None` with message: `No solution`
   - Or: `Infinite solutions`

2. **Type Errors**: Attempting invalid operations returns `None` and prints error message

3. **File Errors**: Missing files are reported with descriptive messages

4. **Dimension Mismatches**: Matrix operations validate dimensions before proceeding

## Implementation Notes

- **Deep Copying**: The solver automatically copies input matrices and vectors to avoid modifying originals
- **Floating Point Precision**: Uses epsilon = 1e-12 for zero comparisons
- **Gaussian Elimination**: Standard forward elimination with back substitution
- **Determinant**: Recursive cofactor expansion for general n×n matrices

## Limitations

- No partial pivoting in current Gaussian elimination (can affect numerical stability)
- Large matrices (n > 100) may experience accumulated floating-point errors
- No support for complex numbers

## Future Enhancements

- [ ] LU decomposition
- [ ] Jacobi iteration method
- [ ] Matrix rank calculation
- [ ] Eigenvalue computation
- [ ] Export results to file
- [ ] Partial pivoting for better numerical stability

## License

MIT License - see LICENSE file for details

---

**Last Updated**: April 2026