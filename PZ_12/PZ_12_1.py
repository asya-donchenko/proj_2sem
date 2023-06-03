num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Вычисляем количество элементов в списке
n = len(num_list)

# Вычисляем индекс разделителя (в данном случае - треть списка)
sep_index = n // 3

# Меняем местами первую и последнюю трети
num_list[:sep_index], num_list[-sep_index:] = num_list[-sep_index:], num_list[:sep_index]

# Выводим результат
print(num_list)