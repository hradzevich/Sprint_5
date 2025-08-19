# Файл используется для хранения фикстур Pytest,
# которые применяются в автотестах сервиса Stellar Burgers
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.registered_user_data import RegisteredUser
from data.urls import *
from used_locators import Locators as loc
from data.registered_user_data import RegisteredUser


# Фикстура для запуска Chrome
@pytest.fixture
def chrome_driver():
    driver = webdriver.Chrome()
    driver.set_window_size(1366, 768)
    yield driver
    driver.quit()


# Фикстура для запуска Firefox
@pytest.fixture
def firefox_driver():
    driver = webdriver.Firefox()
    driver.set_window_size(1366, 768)
    yield driver
    driver.quit()


# Фикстура для автоматического логина зарегистрированного пользователя
# Открывает страницу логина, вводит email и пароль из заранее зарегистрированного пользователя,
# кликает на кнопку "Войти" и возвращает объект драйвера для использования в тестах
@pytest.fixture
def user_logged_driver(chrome_driver):
    chrome_driver.get(LOGIN_PAGE)
    chrome_driver.find_element(*loc.FIELD_EMAIL).send_keys(RegisteredUser.email)
    chrome_driver.find_element(*loc.FIELD_PASSWORD).send_keys(RegisteredUser.password)
    WebDriverWait(chrome_driver, 5).until(EC.element_to_be_clickable((*loc.LOGIN_BTN,)))
    chrome_driver.find_element(*loc.LOGIN_BTN).click()

    WebDriverWait(chrome_driver, 10).until(
        EC.visibility_of_element_located((loc.PLACE_ORDER_BTN))
    )
    return chrome_driver
