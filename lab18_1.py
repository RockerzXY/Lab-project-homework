import urllib.parse
import requests
from secrets import API_KEY
from pprint import pprint
from pathlib import Path
import json


# Конфигурация параметров.
main_api = 'https://www.mapquestapi.com/directions/v2/route?'
orig, dest = 'Washington', 'Baltimore'
key = API_KEY

# Обращение к API.
url = main_api + urllib.parse.urlencode({'key': key, 'from': orig, 'to': dest})
json_data = requests.get(url).json()

# Запись ответа от сервера и вывод в консоль.
with open(Path('files/parsed_route1.json'), 'w') as f:
    json.dump(json_data, f, indent=4)
pprint(json_data)

print(f'URL: {url}')

# Проверка успешности статуса ответа от сервера.
json_status = json_data['info']['statuscode']
if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.\n")
