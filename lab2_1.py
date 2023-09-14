# Задание 1. Создание списка.
ip_list = [
    '127.0.0.1',
    '127.0.0.2'
    '127.0.0.3'
]

# Выведем первый и последний элементы.
print(ip_list[0], ip_list[-1])

# Задание 2. Добавление, удаление и изменение эл-тов списка.
ip_list.append('127.0.0.4')

ip_extended_list = ['20.10.30.10', '20.10.30.20']
ip_list.extend(ip_extended_list)

ip_list.extend('11.22.33 11.33.44'.split())
print(ip_list)

ip_list[0] = '50.50.10.40'
print(ip_list)
