# Задание 1. Форматирование строковых данных.
mac1 = 'Internet 10.220.88.29         94 5254.abbe.5b7b ARPA FastEthernet4'
mac2 = 'Internet 10.220.88.30          3 5254.ab71.e119 ARPA FastEthernet4'
mac3 = 'Internet 10.220.88.32         231 5254.abc7.26aaa ARPA FastEthernet4'

# Подготавливаем строковые переменные к обработке для записи в словарь.
mac_addresses_raw = [mac1.split(), mac2.split(), mac3.split()]
mac_addresses = {}

# Заносим в словарь по родительскому ключу MAC_num
counter = 0
for elem in mac_addresses_raw:
    counter += 1
    mac_addresses[f'MAC_{counter}'] = {'ip': elem[1], 'mac': elem[3]}


# Выводим словарь с данными маршрутизатора в консоль в виде таблицы.
print(f'{"IP АДРЕС":>20}{"MAC АДРЕС":>20}')
print('-' * 20 + ' ' + '-' * 20)
for key, values in mac_addresses.items():
    ip, mac = values['ip'], values['mac']
    print(f"{ip:>20}{mac:>20}")
