import urllib.parse
import requests
from secrets import API_KEY
from pprint import pprint
from pathlib import Path
import json


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
    if json_status == 402:
        print("**********************************************")
        print("Код ошибки: " + str(json_status) + "; Неверный ввод локации. Попробуйте ещё раз.")
        print("**********************************************\n")
    elif json_status == 0:  # Сервер вернул верный запрос.
        route_time = str(json_data['route']['formattedTime']).split(':')
        route_time = f'{route_time[0]} ч. {route_time[1]} м.'

        # Выдача результата пользователю в консоль.
        # Информация о маршруте.
        print('\n           Информация о маршруте')
        print("=============================================")
        print("Маршрут от " + (orig) + " до " + (dest))
        print("Длительность маршрута: " + route_time)
        print("Километров: " + str(int(json_data["route"]["distance"]*1.61)))
        if json_data['route']['hasTunnel']:
            print('Внимание! На маршруте встречаются туннели.')
        if json_data['route']['hasCountryCross']:
            print('Внимание! Придётся пересечь пределы страны.')
        print("=============================================")

        # Список поворотов.
        print('\n               План маршрута')
        print("=============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"]) * 1.61) + " km)"))
        print("=============================================\n")
    else:  # При неизвестной ошибке.
        print("************************************************************************")
        print("Возникла неизвестная ошибка. Код ошибки: " + str(json_status) + "; Посмотрите значения кодов на сайте:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")
