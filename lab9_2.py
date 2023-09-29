# Лаб 9. Задание 2.
from pathlib import Path


with open(Path('files/show_vlan.txt'), 'r') as f:
    data = f.read()
print('Вывод файла show_vlan.txt:\n', data)


vlan = []
flag = 0
for elem in data.split('\n'):
    line_list = list(elem.split())
    if line_list[0].isdigit():
        vlan_elem = (line_list[0], line_list[1])
        vlan.append(vlan_elem)

print('Вывод списка VLAN:\n', vlan)