ip_list = []

for i in range(3):
    ip_list.append(input(f'Введите {i} ip-адрес: '))

for j in range(len(ip_list)):
    print(f'ip-адрес #{j}: {ip_list[j]}')