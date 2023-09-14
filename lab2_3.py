from random import randint, shuffle


# Задание 3. Изменение порядка и сортировка элементов списка.
# Создадим список 1-25 с рандомными значениями
numbers = [randint(1, 25) for i in range(9)]
print('Созданный список:', *numbers)

# Выполним сортировку по убыванию (второй способ закомментирован).
numbers = sorted(numbers, reverse=True)
#numbers = numbers[::-1]
print('Отсортированный по убыванию список:', *numbers, end='\n\n')

# Разрежем список numbers на два списка.
numbers_len = len(numbers)
acl_num1 = numbers[0:(numbers_len // 2)]
acl_num2 = numbers[(numbers_len // 2):]

print('Список 1:', *acl_num1)
print('Список 2:', *acl_num2)

