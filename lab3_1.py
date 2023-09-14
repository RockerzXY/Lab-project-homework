# Задание 1. Преобразование списков в множество и сортировка.
ip_list = [
    '10.1.1.1',
    '10.1.1.1',
    '10.1.1.2',
    '10.1.1.3',
    '10.1.1.3',
    '10.1.1.4',
    '10.1.1.5',
]
ip_addr_unique = set(ip_list)

print('Список IP-адресов:', ip_list)
print('Список уникальных IP-адресов:', ip_addr_unique)

# Преобразование множества в список путём сортировки.
ip_unique_sorted = sorted(ip_addr_unique)
len_ip_list = len(ip_unique_sorted)
print('Сортированный список уникальных IP-адресов:', ip_unique_sorted)
print('Кол-во уникальных IP-адресов:', len_ip_list)
