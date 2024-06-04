#! /usr/bin/python3
"""
A module holding a class representing Sparse Matrix operations
"""

class SparseMatrix:
    def __init__(self, numRows=0, numCols=0, matrixFilePath=None):
        self.elements = {}
        if matrixFilePath:
            self.loadFromFile(matrixFilePath)
        else:
            self.numRows = numRows
            self.numCols = numCols

    def loadFromFile(self, matrixFilePath):
        with open(matrixFilePath, 'r') as file:
            lines = file.readlines()
            self.numRows = int(lines[0].split('=')[1])
            self.numCols = int(lines[1].split('=')[1])
            for line in lines[2:]:
                line = line.strip()
                if line.startswith('(') and line.endswith(')'):
                    row, col, value = map(int, line[1:-1].split(','))
                    self.setElement(row, col, value)
                elif line:  # Non-empty line that does not match expected format
                    raise ValueError("Input file has wrong format")

    def getElement(self, currRow, currCol):
        return self.elements.get((currRow, currCol), 0)

    def setElement(self, currRow, currCol, value):
        if value != 0:
            self.elements[(currRow, currCol)] = value
        elif (currRow, currCol) in self.elements:
            del self.elements[(currRow, currCol)]

    def add(self, other):
        result = SparseMatrix(self.numRows, self.numCols)
        for key, value in self.elements.items():
            result.setElement(key[0], key[1], value + other.getElement(key[0], key[1]))
        for key, value in other.elements.items():
            if key not in self.elements:
                result.setElement(key[0], key[1], value)
        return result

    def subtract(self, other):
        result = SparseMatrix(self.numRows, self.numCols)
        for key, value in self.elements.items():
            result.setElement(key[0], key[1], value - other.getElement(key[0], key[1]))
        for key, value in other.elements.items():
            if key not in self.elements:
                result.setElement(key[0], key[1], -value)
        return result

    def multiply(self, other):
        if self.numCols != other.numRows:
            raise ValueError("Matrix dimensions do not allow multiplication")
        result = SparseMatrix(self.numRows, other.numCols)
        for key1, value1 in self.elements.items():
            for key2, value2 in other.elements.items():
                if key1[1] == key2[0]:
                    result.setElement(key1[0], key2[1], result.getElement(key1[0], key2[1]) + value1 * value2)
        return result

# Example usage:
# matrixA = SparseMatrix(matrixFilePath='path_to_matrix_A.txt')
# matrixB = SparseMatrix(matrixFilePath='path_to_matrix_B.txt')
# matrixC = matrixA.add(matrixB)
# matrixD = matrixA.subtract(matrixB)
# matrixE = matrixA.multiply(matrixB)

