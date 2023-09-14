
# Выявление повторяющихся элементов в списке.
user_input = input('Введите числа через пробел: ')

numbers = list(map(int, user_input.split()))
print('Полученный список:', *numbers)


# Найдём кол-во каждых единиц во всех элементах, разбив по числам.
target_char = '1'
count = 0
for num in numbers:
    for char in list(str(num)):
        if char == target_char:
           count += 1

print('Кол-во единиц:', count)
