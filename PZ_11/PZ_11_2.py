filename = "text18-25.txt"
# Читаем данные из файла
with open(filename, 'r') as f:
    data = f.read()

    # Подсчет количества символов букв в тексте
    letters_count = sum(c.isalpha() for c in data)

    # Удаление буквы 'с' и формирование нового текста в стихотворной форме
    poem = data.replace('с', '')
    poem_lines = poem.split('\n')
    # Форматирование результатов в новый файл
    with open('new_poem.txt', 'w') as new_file:
        new_file.write("{}".format('\n'.join(poem_lines)))
    print("Исходный текст: {}\nКоличество символов букв: {}\nСтихотворный текст:\n{}".format(data, letters_count, poem))


