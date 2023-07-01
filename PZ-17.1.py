class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.data = [[0] * columns for _ in range(rows)]

    def __str__(self):
        matrix_str = ''
        for row in self.data:
            matrix_str += ' '.join(str(element) for element in row) + '\n'
        return matrix_str

    def __add__(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Матрицы имеют разные размеры")

        result = Matrix(self.rows, self.columns)
        for i in range(self.rows):
            for j in range(self.columns):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result

    def __sub__(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Матрицы имеют разные размеры")

        result = Matrix(self.rows, self.columns)
        for i in range(self.rows):
            for j in range(self.columns):
                result.data[i][j] = self.data[i][j] - other.data[i][j]
        return result

    def __mul__(self, other):
        if self.columns != other.rows:
            raise ValueError("Несовместимые размеры матриц для умножения")

        result = Matrix(self.rows, other.columns)
        for i in range(self.rows):
            for j in range(other.columns):
                for k in range(self.columns):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
        return result


# Создание матрицы 2x3
matrix1 = Matrix(2, 3)
matrix1.data = [[1, 2, 3], [4, 5, 6]]
print("Первая матрица:")
print(matrix1)
# Создание матрицы 2x3
matrix2 = Matrix(2, 3)
matrix2.data = [[7, 8, 9], [10, 11, 12]]
print("Вторая матрица:")
print(matrix2)

# Сложение матриц
result_addition = matrix1 + matrix2
print("Сложение матриц:")
print(result_addition)

# Вычитание матриц
result_subtraction = matrix1 - matrix2
print("Вычитание матриц:")
print(result_subtraction)

# Умножение матриц
matrix3 = Matrix(3, 2)
matrix3.data = [[1, 2], [3, 4], [5, 6]]

result_multiplication = matrix1 * matrix3
print("Умножение матриц:")
print(result_multiplication)
