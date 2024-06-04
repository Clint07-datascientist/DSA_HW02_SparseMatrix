# DSA_HW02_SparseMatrix

# Sparse Matrix Operations in Python

This Python project provides an implementation of a sparse matrix data structure that optimizes both memory and runtime while storing large matrices with mostly zero elements. The class supports addition, subtraction, and multiplication of sparse matrices.

## Usage

1. **Installation:**
   - Clone this repository to your local machine.
   - Organize the code and sample input files as follows:
     ```
     /dsa/sparse_matrix/code/src/
     /dsa/sparse_matrix/sample_inputs/
     ```
   - Feel free to organize your files as needed.

2. **SparseMatrix Class:**
   - The `SparseMatrix` class is defined in the `sparse_matrix.py` file.
   - It supports the following methods:
     - `__init__(self, numRows=0, numCols=0, matrixFilePath=None)`: Initializes a sparse matrix.
     - `loadFromFile(self, matrixFilePath)`: Reads a sparse matrix from a file.
     - `getElement(self, currRow, currCol)`: Retrieves an element from the matrix.
     - `setElement(self, currRow, currCol, value)`: Sets an element in the matrix.
     - `add(self, other)`: Performs matrix addition.
     - `subtract(self, other)`: Performs matrix subtraction.
     - `multiply(self, other)`: Performs matrix multiplication.

3. **Input File Format:**
   - The input file format should be as follows:
     ```
     rows=8433
     cols=3180
     (0, 381, -694)
     (0, 128, -838)
     (0, 639, 857)
     ...
     ```
   - The first row specifies the number of rows, the second row specifies the number of columns, and subsequent rows contain non-zero elements.

4. **Error Handling:**
   - The code handles variations in the input file:
     - Ignores whitespaces on some lines.
     - Throws an error if the format is incorrect (e.g., wrong parenthesis or floating-point values).

5. **Example Usage:**
   ```python
   matrixA = SparseMatrix(matrixFilePath='path_to_matrix_A.txt')
   matrixB = SparseMatrix(matrixFilePath='path_to_matrix_B.txt')
   matrixC = matrixA.add(matrixB)
   matrixD = matrixA.subtract(matrixB)
   matrixE = matrixA.multiply(matrixB)

6. **Testing:**
   - Matrices must be compatible for desired operations (e.g dimensions match for multiplication)
   - Test the code using various input files
