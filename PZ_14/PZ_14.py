import re

# Открываем файл для чтения
with open('Dostoevsky.txt', mode='r', encoding='utf-8') as file:
    text = file.read()
    # Используем регулярное выражение для поиска нужных строк
    pattern = re.compile(r'«[А-Я][\w\s]*»')
    matches = pattern.findall(text)

# Выводим найденные строки
for match in matches:
    print(match)

# Выводим количество найденных строк
print(f'Количество произведений: {len(matches)}')