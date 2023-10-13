# Лаб 14. Задание 1.
import privy


# Важно использовать byte формат.
password = b'qwerty'
secret = b'totalsafe'

encrypted_pass = privy.hide(password, secret)
print(f'Зашифрованный пароль: {encrypted_pass}')
decrypted_pass = privy.peek(encrypted_pass, secret).decode('UTF-8')
print(f'Расшифрованный пароль: {decrypted_pass}')