# Лабораторная работа.
from pathlib import Path


text_to_write = 'Первая строка\nВторая строка\nТретья строка\nЧетвёртая строка'
with open(Path('files/classwork11_10.txt'), 'w') as f:
    f.write(text_to_write)

try:
    with open(Path('files/classwork11_10.txt'), 'r') as f:
        data = f.read()
    print(f'Содержимое файла:\n{data}')

    data_list = data.split()
    data_lines = data.split('\n')
    print(f'\nВторое слово: {data_list[1]}')
    print(f'Третья строка: {data_lines[2]}')

    # Запишем в отдельный файл перевёрнутое содержимое текущего файла.
    with open(Path('files/classwork11_10_second.txt'), 'w') as f:
        f.write(data[::-1])



except FileNotFoundError:
    print("Файл не найден")
except IOError:
    print("Файл не найден")
finally:
    # С with не нужно использовать конструкцию file.close().
    f.close()
