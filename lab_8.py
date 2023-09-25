# Циклы. Задание 1.

ip_addr = '172.16.1.1,172.16.2.1,172.16.3.1,172.16.4.1'

ip_list = ip_addr.split(',')

print('Список IP-адресов:')
for elem in ip_list:
    print(elem)


# Задание 2.
print('\nСписок MAC-адресов:')
arp_table = [('10.220.88.1', '0062.ec29.70fe'),
('10.220.88.20', 'c89c.1dea.0eb6'),
('10.220.88.21', '1c6a.7aaf.576c'),
('10.220.88.28', '5254.aba8.9aea'),
('10.220.88.29', '5254.аbаt.5b7b'),
('10.220.88.30', '5254.ab71.e119'),
('10.220.88.32', '5254.abc7.26aa'),
('10.220.88.33', '5254.ab3a.8d26'),
('10.220.88.35', '5254.abfb.af12'),
('10.220.88.37', '0001.00ff.0001'),
('10.220.88.38', '0002.00ff.0001'),
('10.220.88.39', '6464.9be8.08c8'),
('10.220.88.40', '001c.c4bf.826a'),
('10.220.88.41', '001b.7873.5634')]


for elem in arp_table:
    mac_raw = elem[1]
    mac_raw = mac_raw.replace('.', '')

    mac = ''
    counter = 0
    for char in list(mac_raw):
        counter += 1
        mac += char

        if counter == 2:
            counter = 0
            mac += ':'

    mac = mac.upper()[0:-1:]
    print(mac)


# Задание 3.
print('\nСписок сгенерированных IP-адресов:')
ip_list = []
for i in range(1, 255):
    ip_list.append(f'10.10.100.{i}')


for i, ip in enumerate(ip_list, start=0):
    print(f'{i} ---> {ip}')


print('\nСрезанные IP-адреса:')
new_ip_addresses = ip_list[2:6]
for ip in new_ip_addresses:
    print(ip)
