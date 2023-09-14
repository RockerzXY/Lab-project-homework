# Задание 1. Манипуляции со строками
show_version = ' *0 CISCO881-SEC-K9 FTX0000038X    '

# Удалим все пробелы.
show_version = show_version.strip()
print(show_version, end='\n\n')

show_version_list = show_version.split()
model, serial_number = show_version_list[1], show_version_list[2]


print('Наличие Cisco: ', end='')
if 'cisco' in model.lower():
    print(True)
else:
    print(False)

print('Наличие 881 в серийном номере: ', end='')
if '881' in serial_number:
    print(True)
else:
    print(False)

print('Модель:', model)
print('Серийный номер', serial_number)