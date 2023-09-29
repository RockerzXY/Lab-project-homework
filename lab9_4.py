# Лаб 9. Задание 4.
from pathlib import Path


with open(Path('files/show_lldp_neighbors_detail.txt'), 'r') as f:
    data = f.read()

sys_name, port_id = '', ''
for elem in data.split('\n'):
    elem_list = elem.split(': ')

    if elem_list[0] == 'System Name':
        sys_name = elem_list[1]
    elif elem_list[0] == 'Port id':
        port_id = elem_list[1]

print(f'System Name: {sys_name} | Port ID: {port_id}')
