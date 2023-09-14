from random import randint


# Задание 2. Операции со множествами.
vlan_mos = [randint(1, 10) for i in range(8)]
vlan_kursk = [randint(1, 15) for j in range(10)]
vlan_novosib = [randint(1, 20) for k in range(15)]

print('VLAN в Москве:', *vlan_mos)
print('VLAN в Курске:', *vlan_kursk)
print('VLAN в Новосибирске:', *vlan_novosib, end='\n\n')


vlan_mos = set(vlan_mos)
vlan_kursk = set(vlan_kursk)
vlan_novosib = set(vlan_novosib)

print('Кол-во уникальных VLAN в Москве:', len(vlan_mos), end='\n\n')

print('Уникальные VLAN в Москве:', *vlan_mos)
print('Уникальные VLAN в Курске:', *vlan_kursk)
print('Уникальные VLAN в Новосибирске:', *vlan_novosib, end='\n\n')


# Ищем одинаковые VLAN между Москвой и Курском.
print('Одинаковые VLAN между МСК-КУРС:', *(vlan_mos & vlan_kursk))

# Ищем одинаковые VLAN во всех городах.
print('Одинаковые VLAN во всех городах:', *(vlan_mos & vlan_kursk & vlan_novosib))

# Ищем уникальные VLAN в Новосибирске.
print('Уникальные VLAN в Новосибирске:', *(vlan_novosib - (vlan_mos | vlan_kursk)))
