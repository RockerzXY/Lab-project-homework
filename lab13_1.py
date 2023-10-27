# Лаб 13. Задание 1.
import ipaddress


user_ip = ipaddress.IPv4Address(input('Введите IP адрес в формате число-точка: '))
user_prefix_length = int(input('Введите длину сетевого префикса (от 0 до 32): '))

# Определение адреса классовой сети и класса сети.
network = ipaddress.IPv4Network(f'{user_ip}/{user_prefix_length}', strict=False)
network_address = network.network_address

ip = ipaddress.IPv4Address(user_ip)
network_class_name = 'None'
first_byte = ip.packed[0]  # Получаем первый байт.
if 1 <= first_byte <= 126:
    network_class_name = 'A'
elif 128 <= first_byte <= 191:
    network_class_name = 'B'
elif 192 <= first_byte <= 223:
    network_class_name = 'C'
elif 224 <= first_byte <= 239:
    network_class_name = 'D'
elif 240 <= first_byte <= 255:
    network_class_name = 'E'
print(f'Адрес классовой сети: {network_address}')
print(f'Класс сети: {network_class_name}')

# Определение адреса подсети.
subnet = network.subnets(prefixlen_diff=3)
subnets = [str(s) for s in subnet]
print(f'Адрес подсети: {subnets[0]}')

# Определение и вывод диапазона адресов, первого и последнего.
first_ip = network_address + 1
last_ip = network_address + (2 ** (32 - user_prefix_length) - 2)
print(f'Первый адрес в диапазоне: {first_ip}')
print(f'Последний адрес в диапазоне: {last_ip}')

# Определение и вывод broadcast адреса.
broadcast_address = network.broadcast_address
print(f'Broadcast адрес: {broadcast_address}')


# Разбиение на три подсети (Теперь работает).
subnets = []
for i in range(3):
    subnets.append(list(network.subnets(prefixlen_diff=(i + 1))))

for i, subnet in enumerate(subnets):
    print(f'\n[Подсеть {i + 1}]')
    for j, net in enumerate(subnets[i]):
        print(f'Сеть {j + 1}: {net[j]}')
