# Лаб 9. Задание 3.
from pathlib import Path


with open(Path('files/show_arp.txt'), 'r') as f:
    data = f.read()
data = data.split('\n')[1:]

flag = 0
print('Выведем все IP и MAC адреса:')
for elem in data:
    elem_list = list(elem.split())
    ip, mac = elem_list[1], elem_list[3]

    if ip == '10.220.88.1':
        flag += 1
        print(f'Default gateway IP/MAC is ---> IP: {ip} | MAC: {mac}')
    elif ip == '10.220.88.30':
        flag += 1
        print(f'Arista 3 IP/MAC is ---> IP: {ip} | MAC: {mac}')
    elif flag == 2:
        break
    # Мы это не выводим, так как в представленном выводе нет остальных строк, кроме искомых?
    # else:
    #     print(f'IP: {ip} | MAC: {mac}')


