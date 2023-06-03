string = "ab12c3d45"

def digits_only(string):
    # Цикл по символам в строке
    for char in string:
        # Если символ - цифра, передаем ее генератору
        if char.isnumeric():
            yield char

digits = digits_only(string)
for digit in digits:
    print(digit, end=' ')