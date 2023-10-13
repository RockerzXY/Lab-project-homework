# Лаб 12. Задание 1.

def ssh_conn(ip, username, password):
    print(f'IP-адрес: {ip}\nUsername: {username}\nPassword: {password}\n')


# Позиционные аргументы.
ssh_conn('192.168.1.1', 'admin', 'qwerty')
# Именованные аргементы.
ssh_conn(username='root', password='qwerty123', ip='127.0.0.1')
# Сочетание двух методов.
ssh_conn('0.0.0.1', password='AAAAAAAAAAA', username='toor')
