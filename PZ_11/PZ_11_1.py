import random

filename1 = "file1.txt"
filename2 = "file2.txt"
with open(filename1, 'w') as f1, open(filename2, 'w') as f2:
    sequence1 = [random.randint(-100, 100) for _ in range(10)]
    sequence2 = [random.randint(-100, 100) for _ in range(10)]
    f1.write('\n'.join(map(str, sequence1)))
    f2.write('\n'.join(map(str, sequence2)))

with open(filename1, 'r') as f1, open(filename2, 'r') as f2, open("result.txt", 'w') as res:
    data1 = f1.read().splitlines()
    data2 = f2.read().splitlines()

    # Функция для обработки данных из файлов
    def process_data(data):
        data_list = list(map(int, data))
        sorted_list = sorted(data_list)
        count = len(data_list)
        min_mult_2 = min(filter(lambda x: x % 2 == 0, data_list))
        max_mult_5 = max(filter(lambda x: x % 5 == 0, data_list))
        return data_list, sorted_list, count, min_mult_2, max_mult_5

    # Обработка данных из файлов
    data1_list, sorted1_list, count1, min2_1, max5_1 = process_data(data1)
    data2_list, sorted2_list, count2, min2_2, max5_2 = process_data(data2)

    # Запись результата в новый файл
    res.write("Элементы первого файла: {}\n".format(data1_list))
    res.write("Элементы второго файла: {}\n".format(data2_list))
    res.write("Элементы после сортировки: {} {}\n".format(sorted1_list, sorted2_list))
    res.write("Количество элементов: {} {}\n".format(count1, count2))
    res.write("Минимальный элемент кратный 2: {} {}\n".format(min2_1, min2_2))
    res.write("Максимальный элемент кратный 5: {} {}\n".format(max5_1, max5_2))