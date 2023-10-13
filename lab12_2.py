# Лаб 12. Задание 2.

def ssh_conn2(ip, username, password, device_type='huawei_vrp'):
    print(f'IP-адрес: {ip}\nUsername: {username}\nPassword: {password}\nDevice: {device_type}\n')

def ssh_conn3(device_type='huawei_vrp', **kwargs):
    print(f'IP-адрес: {kwargs["ip"]}\nUsername: {kwargs["username"]}\nPassword: {kwargs["password"]}\nDevice: {device_type}\n')


# Позиционные аргументы.
ssh_conn2('192.168.1.1', 'admin', 'qwerty')
# Именованные аргементы.
ssh_conn2(username='root', password='qwerty123', ip='127.0.0.1')
# Сочетание двух методов.
ssh_conn2('0.0.0.1', password='AAAAAAAAAAA', username='toor')
# Используем **kwargs в функции.
ssh_conn3(username='white', password='he-he-he', ip='127.0.0.1')
