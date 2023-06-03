matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

# находим размер матрицы
n = len(matrix)

# возводим элементы второго столбца в квадрат
for i in range(n):
    if i == 1:
        for j in range(n):
            matrix[i][j] = matrix[i][j] ** 2

print("Матрица после возведения в квадрат элементов второго столбца:")
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()