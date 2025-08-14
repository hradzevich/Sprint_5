import pytest
from selenium import webdriver
import random as r
from faker import Faker


# Фикстура для запуска Chrome
@pytest.fixture
def chrome_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


# Фикстура для запуска Firefox
@pytest.fixture
def firefox_driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


# Фикстура для генерации данных(имя, логин, пароль) для регистрации
@pytest.fixture
def credentials_for_registration():
    # Объявляем переменную, предсталяющую собой список доменов
    domains = ["yandex.ru", "gmail.com", "yahoo.com", "mail.ru"]
    # Объявляем переменную, предсталяющую собой строку из символов для генерации пароля
    numbers_plus_letters = "1234567890abcdefghijklmnopqrstuvwxyz"
    # Генеририуем логин по заданному формату имя_фамилия_номер когорты_любые3цифры@домен
    login = "hanna_radzevich_28_" + str(r.randint(100, 999)) + "@" + r.choice(domains)
    # Генерируем пароль длиной 9 символов
    password = "".join(r.sample(numbers_plus_letters, 9))
    # Создаём объект Faker с русской локалью
    fake = Faker("ru_RU")
    # Генерируем полное имя (Имя + Фамилия)
    name = f"{fake.first_name()} {fake.last_name()}"
    return {"login": login, "password": password, "name": name}


# Фикстура для создания логина и пароля для логина уже зарегистрированного пользователя
@pytest.fixture
def credentials():
    return {
        "login": "hanna_radzevich_28_123@yandex.com",
        "password": "password123",
    }
