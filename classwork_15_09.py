# Работа на паре 15.09.2023
# Задание 1. Создание словаря и работа с  его методами.
d = dict.fromkeys(['a', 'b'], 100)
print(d)

d = dict(short='dict', long='dictionary')
print(d)

d = {a: a ** 2 for a in range(7)}
print(d)


# Получаем два списка: ключи и значения.
keys = list(d.keys())
values = list(d.values())
print(keys, values)

# Скопируем словарь.
d_copy = d.copy()
print(d_copy)

# Очистим словарь.
d.clear()

# Вернём значения из копии.
d = d_copy
print(d.get(6))

# Удалим ключ и значение.
d.pop(6)
print(d)
d_deleted = d.popitem()
print(d)
print('deleted item', d_deleted)



# Задание 2. Задачи:
# 1. Обработка исключения DivisionZero
number = input('Введите число: ')
if not number.isdigit():
    print('Это должно быть число!')
    exit()
number = int(number)

try:
    print(f'Делим целочисленно 144 на {number}. Ответ:', 144 // number, end='\n\n')
except ZeroDivisionError:
    print('Ошибка деления на ноль')
    exit()


# 2. Поиск буквы в тексте переменной, которой вводит пользователь.
text = input('Введите любой текст: ')
target = input('Введите символ, который будем искать: ')

print('Факт нахождения: ', end='')
if target in text:
    print(True)
else:
    print(False)
print('Кол-во:', text.count(target), end='\n\n')


# 3. Проверка вводимого пароля и есть ли в пароле имя пользователя.
inp_name = input('Введите имя пользователя: ')
inp_pass = input('Введите текстовый пароль: ')

if len(inp_pass) <= 8:
    print('Пароль должен быть больше 8 символов.')
    exit()

if inp_name in inp_pass:
    print('Пароль не должен содержать имя пользователя')
    exit()
else:
    print('Пароль принят')
