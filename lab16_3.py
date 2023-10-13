# Лаб 16. Задание 3.
from pathlib import Path
import re


with open(Path('files/show_ipv6_intf.txt'), 'r') as f:
    data = f.read()


ipv6_pattern = r'\b[0-9a-fA-F:]+/[0-9]+\b'
ipv6_addresses = re.findall(ipv6_pattern, data)

ip_1 = ipv6_addresses[0]
ip_2 = ipv6_addresses[1]

print(f'{ip_1}\n{ip_2}')
