import random
import string
def generate_password(lenght=12):
    # Все возможные символы для пароля
    all_chars = string.ascii_letters + string.digits + string.punctuation

     # Генерация пароля нужной длины
    password = ''.join(random.choice(all_chars) for _ in range(lenght))
    return password

# Пример использования
password = generate_password(12)
print("Сгенерированный пароль:" , password)




