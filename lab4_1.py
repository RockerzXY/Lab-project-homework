# Задание 1. Работа со словарями.

device = {
    'ip': '10.10.20.12',
    'username': 'user',
    'password': 'pass',
}

print(device.get('password'))

# Создадим список ключей словаря device.
device_key = list(device.keys())

# Создадим список значений словаря device.
device_value = list(device.values())

print('Ключи словаря device:', *device_key)
print('Значения словаря device:', *device_value)


add_config = {
    'device_type': 'huawei',
    'session_log': 'output.txt',
}

device.update(add_config)
print('\nВыведем обновлённый словарь:')
for elem in device:
    print(f'{elem}: {device[elem]}')
