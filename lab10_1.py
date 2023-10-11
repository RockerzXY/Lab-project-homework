# Лаб 10. Парсинг JSON.
import json
from pprint import pprint
from pathlib import Path


# Задание 1.
with open(Path('files/interface-config.json')) as f:
    data = f.read()

data = data.strip()
print(f'Тип хранимого текста: {type(data)}')

json_data = json.loads(data)
print('Вывод json_data с помощью pprint:')
pprint(json_data)

