# Лаб 16. Задание 2.
import re


data = '''
Cisco 881 (MPC8300) processor (revision 1.0) with 236544K/25600K bytes of 
memory.
Processor board ID FTX0000038X
5 FastEthernet interfaces
1 Virtual Private Network (VPN) Module
256K bytes of non-volatile configuration memory.
126000K bytes of ATA CompactFlash (Read/Write)
'''

model = re.search(r'Cisco \d+ \((.*?)\)', data).group(1)
memory = re.search(r'with (\d+K/\d+K) bytes', data).group(1)

print('-' * 20)
print(f'Model: {model}\nMemory: {memory}')
print('-' * 20)
