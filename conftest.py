import pytest
from selenium import webdriver
from generation_user_data import UserDataGenerator
from registered_user_data import RegisteredUser


# Фикстура для запуска Chrome
@pytest.fixture
def chrome_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


# Фикстура для запуска Firefox
@pytest.fixture
def firefox_driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


# Фикстура для генерации данных(имя, логин, пароль) для регистрации
@pytest.fixture
def user_data():
    generator = UserDataGenerator()
    return generator.generate_user_data()


# Фикстура для создания логина и пароля для логина уже зарегистрированного пользователя
@pytest.fixture
def registered_user():
    user = RegisteredUser()
    return user.get_registered_user()
