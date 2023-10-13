# Лаб 12. Задание 3.
from random import randint

def generate_ip(*args, **kwargs):
    ip = None
    if args:
        if len(args) == 0:
            ip = f'192.168.1.{randint(1, 254)}'
        elif len(args) == 3:
            ip =f'{args[0]}.{args[1]}.{args[2]}.{randint(1, 254)}'
        else:
            return 'Передай только три октета!'

    elif kwargs:
        if len(kwargs) == 0:
            ip = f'192.168.1.{randint(1, 254)}'
        elif len(kwargs) == 3:
            ip = f'{kwargs["octet1"]}.{kwargs["octet2"]}.{kwargs["octet3"]}.{randint(1, 254)}'
        else:
            return 'Передай только три октета!'
    else:
        ip = f'192.169.1.{randint(1, 254)}'
    return ip


print(generate_ip())
print(generate_ip(192, 1, 1))
print(generate_ip(octet1=172, octet2=16, octet3=4))
print(generate_ip(192, 168, 1, 1))
