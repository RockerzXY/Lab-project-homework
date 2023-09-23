import ipaddress
# Лаб 7. Задание 1.


ip_user = input('Введите IP-адрес форматом десятичное с точкой: ')
ipv4_classes = {'A': {'start': '1.0.0.0', 'end': '127.255.255.255'},
                'B': {'start': '128.0.0.0', 'end': '191.255.255.255'},
                'C': {'start': '192.0.0.0', 'end': '223.255.255.255'},
                'D': {'start': '224.0.0.0', 'end': '239.255.255.255'},
                'E': {'start': '240.0.0.0', 'end': '255.255.255.255'}}


# Решение 1.
print('Метод 1.')
ip_octets = list(map(int, ip_user.split('.')))

if len(ip_octets) != 4:
    print('IPv4-адрес содержит только 4 октета! Перезапустите скрипт.')
else:
    first_octet = ip_octets[0]
    for key, elem in ipv4_classes.items():
        start_ip = ipaddress.IPv4Address(elem['start'])
        end_ip = ipaddress.IPv4Address(elem['end'])

        if start_ip <= ipaddress.IPv4Address(ip_user) <= end_ip:
            print(f'IP-адрес принадлежит классу {key}.')
            break
    else:
        print(f'Введённый IP-адрес не соответствует никакому из классов IPv4.')


# Решение 2. С использованием подключаемой библиотеки.
print('\nМетод 2.')
ip = ipaddress.IPv4Address(ip_user)
first_byte = ip.packed[0]  # Получаем первый байт.
if 1 <= first_byte <= 126:
    print(f'IP-адрес принадлежит классу A.')
elif 128 <= first_byte <= 191:
    print(f'IP-адрес принадлежит классу B.')
elif 192 <= first_byte <= 223:
    print(f'IP-адрес принадлежит классу C.')
elif 224 <= first_byte <= 239:
    print(f'IP-адрес принадлежит классу D.')
elif 240 <= first_byte <= 255:
    print(f'IP-адрес принадлежит классу E.')
else:
    print(f'Введённый IP-адрес не соответствует никакому из классов IPv4.')





