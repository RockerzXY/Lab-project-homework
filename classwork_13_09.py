from datetime import datetime
from random import randint, shuffle


# Программа приветствия
name = input('Введите имя: ')
print(f'Привет, {name}', end='\n\n')


# Определение возраста по году.
year_input = int(input('Введите возраст: '))
year = datetime.today().year
print('Год рождения:', year - year_input - 1, end='\n\n')



# Лаб. 2; Работа со списками.
chars = []
for i in range(10):
    chars.append(i)

print('Список чисел:', *chars)
print('Длина списка:', len(chars))

print('Первый и последний элементы:', chars[0], chars[-1])

numbers = [100, 200]
chars.extend(numbers)
numbers.clear()
print('Добавили два элемента:', *chars)
chars.pop(-1)
chars.pop(-1)
print('Убрали из списка', *chars, end='\n\n')


numbers = [randint(1, 25) for i in range(50)]
print('Создадим список 1-25 с рандомными значениями:', *numbers)
numbers = sorted(numbers, reverse=True)
print('Отсортируем по убыванию', *numbers, end='\n\n')

# Выявление повторяющихся элементов в списке.
user_input = input('Введите числа через пробел: ')

numbers = list(map(int, user_input.split()))
print('Полученный список:', *numbers)

# Проверка на пустоту списка, вычисление произведения эл-тов.
if not numbers:
    print('Список пуст.')
else:
    res = 1
    for elem in numbers:
        res *= elem
    print('Найдём произведение элементов списка:', res, end='\n\n')


# Лаб 2. Работа с кортежами.
langs = ('ru', 'ch', 'it')
print('Созданный кортеж:', *langs)

# Дополняем кортеж.
langs_upd = (*langs, 'en')
print('Обновлённый кортеж:', langs_upd)

# Преобразуем кортеж и заменяем нужный элемент.
langs_upd = list(langs_upd)
langs_upd[langs_upd.index('it')] = 'tea'
langs_upd = tuple(langs_upd)
print('Преобразованный кортеж:', langs_upd, end='\n\n')


# Лаб 2. Работа со множествами.
numbers = [randint(1, 100 + 1) for i in range(25)]
print('Рандомные числа в списке:', *numbers)

len_list = len(numbers)
numbers = set(numbers)
len_set = len(numbers)

print('Преобразуем в множество:', numbers)
print(f'Длина списка = {len_list}\nДлина множества {len_set}')

# Лаб 2. Задание ко множествам.
user_input_set = set(map(int, input('\nВведите 2 числа через пробел: ')))

# 1. Есть ли уникальные числа в пользовательском вводе.
if not user_input_set:
    print('Числа не введены')
else:
    if len(user_input_set) == 1:
        print('Введены два одинаковых числа')
    elif len(user_input_set) == 2:
        print('Введённые числа уникальны')
