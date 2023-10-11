# Лаб 10. Задание 3.
import json
from pathlib import Path
from pprint import pprint


with open(Path('files/interfaces.json')) as f:
    json_data = json.loads(f.read())

pprint(json_data)

print('\nИмена интерфейсов:')
for count, interface in enumerate(json_data['ietf-interfaces:interfaces']['interface'], start=1):
    print(f"{count}. {interface['name']}")

print('\nIP-адреса интерфейсов:')
for interface in json_data['ietf-interfaces:interfaces']['interface']:
    ip, mask = None, None
    if 'address' in interface['ietf-ip:ipv4']:
        ip, mask = interface['ietf-ip:ipv4']['address'][0]['ip'], interface['ietf-ip:ipv4']['address'][0]['netmask']
    print(f'{interface["name"]}: {ip}, {mask}')
