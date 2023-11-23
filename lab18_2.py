import urllib.parse
import requests
from secrets import API_KEY
from pprint import pprint



# Конфигурация параметров.
main_api = 'https://www.mapquestapi.com/directions/v2/route?'
key = API_KEY
QUIT_COMMANDS_LIST = ['quit', 'q']

def want_quit(a):
    if a in QUIT_COMMANDS_LIST:
        return True
    return False

while True:
    # Запрос от пользователя точек маршрута.
    print(f"[Выберите локации маршрута; Для выхода напишите '{QUIT_COMMANDS_LIST[0]}']")
    orig = input('Откуда: ')
    if want_quit(orig):  # Проверка на то, хочет ли пользователь выйти.
        print('( До встречи! )')
        break

    dest = input('Куда: ')
    if want_quit(dest):  # Проверка на то, хочет ли пользователь выйти.
        print('( До встречи! )')
        break
    print('\n[Обращаемся к серверу...]')

    # Обращение к API.
    url = main_api + urllib.parse.urlencode({'key': key, 'from': orig, 'to': dest})
    json_data = requests.get(url).json()

    # Проверка успешности обращения к серверу.
    json_status = json_data['info']['statuscode']
    if json_status != 0:
        print('{Что-то пошло не так. Попробуйте ещё раз}\n\n')
    else:
        # Выдача результата пользователю в консоль.
        pprint(json_data)
        print('\n')

