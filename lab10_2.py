# Лаб 10. Задание 2.
import json
from pathlib import Path
from pprint import pprint


with open(Path('files/interface-config.json')) as f:
    json_data = json.loads(f.read())

pprint(json_data)
print('\nВыведем только ietf_interfaces:interface:')
pprint(json_data['ietf-interfaces:interface'])

ip = json_data['ietf-interfaces:interface']['ietf-ip:ipv4']['address'][0]['ip']
print(f'\nИзвлечённый IP-адрес: {ip}')
