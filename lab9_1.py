# Лаб 9. Задание 1.
from pathlib import Path


print('Вывод файла devices.txt:')
with open(Path('files/devices.txt'), 'r') as f:
    data = f.read()
print(data.strip())

print('Вывод списка девайсов:')
list_devices = list(data.split('\n')[:-1])
print(list_devices)


print('Выводим и записываем изменённый файл:')
data = '\n' + data + '\n'
print(data)
with open(Path('files/devices.txt'), 'w') as f:
    f.write(data)




