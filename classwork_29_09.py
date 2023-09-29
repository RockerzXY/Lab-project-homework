# Работа на лекции.
from pathlib import Path

# Задание 1.
with open(Path('files/file_4_1.txt'), 'r') as f:
    data = f.read()
#print(data, '\n')

interfaces = {}
for elem in data.split('\n')[1:]:
    elem_list = list(elem.split())
    interface, ip = elem_list[0], elem_list[1]

    if ip != 'unassigned':
        interfaces[interface] = ip

for key, elem in interfaces.items():
    print(f'{key}: {elem}')
print()


# Задание 2.
with open(Path('files/file_4_2.txt'), 'r') as f:
    data = f.read()
#print(data, '\n')
data = data.strip()

addresses = []
for elem in data.split('\n')[6:]:
    elem_list = list(elem.split())
    address = (elem_list[0], elem_list[1], elem_list[2])
    addresses.append(address)
addresses = sorted(addresses, key=lambda x: [int(x[0])])
print(addresses)

user_vlan = input('Введите VLAN для поиска: ')
for elem in addresses:
    if user_vlan == elem[0]:
        print(*elem)
        break
else:
    print('VLAN не найден.')

