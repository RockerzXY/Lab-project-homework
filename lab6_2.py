from tabulate import tabulate


ip_user = input('Введите IP-адрес через точку: ')
octets_list = list(map(int, ip_user.split('.')))

# Проверка на правильное написание IPv4 адреса.
if len(octets_list) != 4:
    print('IPv4-адрес содержит только 4 октета! Перезапустите скрипт.')
    exit()


# Создание вложенного списка с заголовками для будущей таблицы.
table_data = [['Octets'], ['Decimal'], ['Binary'], ['Hex']]
counter = 0
# Запись данных в таблицу.
for elem in octets_list:
    counter += 1
    oct_dec, oct_bin, oct_hex = elem, bin(elem), hex(elem)
    table_data[0].append(f'Octet_{counter}')
    table_data[1].append(oct_dec)
    table_data[2].append(oct_bin)
    table_data[3].append(oct_hex)


# Используем стороннюю библиотеку для удобного построения таблицы.
table_octets = tabulate(table_data, headers='firstrow', tablefmt="grid")
print(table_octets)
