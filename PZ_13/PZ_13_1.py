matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

# находим размер матрицы
n = len(matrix)

# находим половину матрицы
half = n // 2

# суммируем элементы второй половины матрицы
sum = 0
for i in range(half, n):
    for j in range(n):
        sum += matrix[i][j]

print("Сумма элементов второй половины матрицы: ", sum)