# Данный файл содержит метод generate_user_data, который используется для генерации
# тестовых данных (имя, email и пароль) для автотестов сервиса Stellar Burgers
import random as r
from faker import Faker


faker = Faker("ru_RU")  # Создаём объект Faker с русской локалью


def generate_user_data():

    # Генерируем полное имя (Имя + Фамилия)
    name = f"{faker.first_name()} {faker.last_name()}"

    # Объявляем переменную, представляющую собой список доменов
    domains = ["@yandex.ru", "@gmail.com", "@yahoo.com", "@mail.ru"]

    # Генеририуем логин по заданному формату имя_фамилия_номер когорты_любые3цифры@домен
    email = "hanna_radzevich_28_" + str(r.randint(100, 999)) + r.choice(domains)

    # Объявляем переменную для генерации паролей длиной от 6 до 12 символов
    password_length = r.randint(6, 12)

    # Генерируем пароль длиной password_length
    password = faker.password(
        length=password_length,
        special_chars=True,
        digits=True,
        upper_case=True,
        lower_case=True,
    )

    # Возвращаем данные в виде кортежа
    return name, email, password
