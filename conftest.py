# Файл используется для хранения фикстур Pytest,
# которые применяются в автотестах сервиса Stellar Burgers

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from generation_user_data import UserDataGenerator
from registered_user_data import RegisteredUser
from tests import urls
from tests import used_locators as loc


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


# Фикстура для автоматического логина зарегистрированного пользователя
# Открывает страницу логина, вводит email и пароль из заранее зарегистрированного пользователя,
# кликает на кнопку "Войти" и возвращает объект драйвера для использования в тестах
@pytest.fixture
def user_logged_driver(chrome_driver, registered_user):
    chrome_driver.get(urls.login_url)
    chrome_driver.find_element(*loc.Locators.field_email).send_keys(
        registered_user["email"]
    )
    chrome_driver.find_element(*loc.Locators.field_password).send_keys(
        registered_user["password"]
    )
    WebDriverWait(chrome_driver, 5).until(
        EC.element_to_be_clickable((*loc.Locators.login_btn,))
    )
    chrome_driver.find_element(*loc.Locators.login_btn).click()

    WebDriverWait(chrome_driver, 10).until(
        EC.visibility_of_element_located((loc.Locators.place_order_btn))
    )
    return chrome_driver
