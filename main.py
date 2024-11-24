import random
import string


def generate_password(lenght=12):
    # Буквы и цифры
    chars = string.ascii_letters + string.digits
    # Все возможные символы для пароля
    all_chars = chars + '!#$%&*-_+-='

    # Генерация первого символа
    password = random.choice(chars)
    # Генерация пароля нужной длины
    password += ''.join(random.choice(all_chars) for _ in range(lenght - 1))
    return password


if __name__ == '__main__':
    # Пример использования
    password = generate_password(12)
    print('Сгенерированный пароль:', password)
if __name__ == '__main__':
    # Ввод длины пароля пользователем
    try:
        user_length = int(input("Введите длину пароля (не менее 6 символов): "))
        if user_length < 6:
            print("Длина пароля должна быть не менее 6 символов.")
        else:
            password = generate_password(user_length)
            print('Сгенерированный пароль:', password)
    except ValueError:
        print("Пожалуйста, введите целое число.")