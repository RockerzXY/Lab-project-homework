# Лаб 16. Зададание 1.
from pathlib import Path
import re


with open(Path('files/show_version.txt'), 'r') as f:
    data = f.read()

ios_version = re.search(r'IOS Software, ([^,]+)', data).group(1)
serial_number = re.search(r'Version ([^,]+)', data).group(1)
config_register = re.search(r'Configuration register is (\S+)', data).group(1)

print("Версия IOS:", ios_version)
print("Серийный номер:", serial_number)
print("Конфигурационный регистр:", config_register)
