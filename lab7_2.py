# Лаб 2. Задание 2.

mask_input = input('Введите маску в формате число-точка без пробелов: ')

octets = mask_input.split('.')
if len(octets) != 4:
    print('В маске может быть четыре октета.')
else:
    valid_mask = True
    for octet in octets:
        if not (0 <= int(octet) <= 255):
            print('Октет может иметь лишь значение в диапазоне 0-255.')
            valid_mask = False
            break

    if valid_mask:
        binary_mask = ''.join([bin(int(octet))[2:].zfill(8) for octet in octets])
        count = binary_mask.count('1')

        cidr_notation = '/' + str(count)

        print(f'Префикс маски подсети {mask_input}: {cidr_notation}')
