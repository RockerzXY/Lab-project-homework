# Лаб 12. Задание 5.

data = []
while True:
    user_inp = input()
    if user_inp != 'end':
        data.append(user_inp)
    else:
        break

print(list(filter(lambda x: x.isalpha(), data)))
