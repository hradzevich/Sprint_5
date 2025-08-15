import random as r
from faker import Faker


class UserDataGenerator:
    def __init__(self):
        self.name = None
        self.email = None
        self.password = None
        self.fake = Faker("ru_RU")  # Создаём объект Faker с русской локалью

    def generate_user_data(self):
        if self.name is None and self.email is None and self.password is None:

            # Генерируем полное имя (Имя + Фамилия)
            self.name = f"{self.fake.first_name()} {self.fake.last_name()}"

            # Объявляем переменную, представляющую собой список доменов
            domains = ["@yandex.ru", "@gmail.com", "@yahoo.com", "@mail.ru"]

            # Генеририуем логин по заданному формату имя_фамилия_номер когорты_любые3цифры@домен
            self.email = (
                "h_radzevich_28_" + str(r.randint(100, 999)) + r.choice(domains)
            )

            # Объявляем переменную, предсталяющую собой строку из символов для генерации пароля
            numbers_plus_letters = "1234567890abcdefghijklmnopqrstuvwxyz"

            # Объявляем переменную для генерации паролей длиной от 6 до 12 символов
            password_length = r.randint(6, 12)

            # Генерируем пароль длиной password_length
            self.password = "".join(r.sample(numbers_plus_letters, password_length))

            # Возвращаем данные в виде словаря
            return {"name": self.name, "email": self.email, "password": self.password}
