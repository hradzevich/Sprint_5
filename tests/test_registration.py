from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import register_url, login_url
from used_locators import Locators as loc
import random as r


class TestRegistrationSuccess:
    # Проверка регистрации нового пользователя с валидными логином(email в формате логин@домен) и паролем(длина более 6 символов)
    def test_registration_valid_credentials_success(self, chrome_driver, user_data):

        # Откроем страницу регистрации в окне браузера
        chrome_driver.get(register_url)

        # Введем в поле "Имя" значение имени пользователя
        chrome_driver.find_element(*loc.field_name).send_keys(user_data["name"])

        # Сохраним в переменную email значение email пользователя, которое далее используем для входа
        email = user_data["email"]

        # Введем в поле "Еmail" значение email пользователя
        chrome_driver.find_element(*loc.field_email).send_keys(email)

        # Сохраним в переменную password значение пароля пользователя, которое далее используем для входа
        password = user_data["password"]

        # Введем в поле "Пароль" значение пароля пользователя
        chrome_driver.find_element(*loc.field_password).send_keys(password)

        # Кликнем на кнопку "Зарегистрироваться"
        chrome_driver.find_element(*loc.registration_btn).click()

        # Ждём и проверяем, что URL изменился на страницу логина
        assert WebDriverWait(chrome_driver, 10).until(EC.url_to_be(login_url))


class TestRegistrationInvalisPassword:
    # Проверка появления ошибки при регистрации нового пользователя с валидными логином(email в формате логин@домен) и паролем, длина которого менее 6 символов
    def test_registration_invalid_password_error(self, chrome_driver, user_data):

        # Откроем страницу регистрации в окне браузера
        chrome_driver.get(register_url)

        # Введем в поле "Имя" значение имени пользователя
        chrome_driver.find_element(*loc.field_name).send_keys(user_data["name"])

        # Введем в поле "Еmail" значение email пользователя
        chrome_driver.find_element(*loc.field_email).send_keys(user_data["email"])

        # Сгенерируем переменную password с невалидным значением пароля пользователя (длина 5 символов)
        numbers_plus_letters = "1234567890abcdefghijklmnopqrstuvwxyz"
        password = "".join(r.sample(numbers_plus_letters, 5))

        # Введем в поле "Пароль" значение пароля пользователя
        chrome_driver.find_element(*loc.field_password).send_keys(password)

        # Кликнем на кнопку "Зарегистрироваться", чтобы снять фокус с поля "Пароль"
        chrome_driver.find_element(*loc.registration_btn).click()

        # Добавим явное ожидание, что ошибка некорректного пароля отображается
        WebDriverWait(chrome_driver, 10).until(
            EC.visibility_of_element_located((loc.password_error_message))
        )

        # Находим элемент с сообщением об ошибке при некорректном пароле
        incorrect_password_error = chrome_driver.find_element(
            *loc.password_error_message
        )

        # Проверка, что элемент ошибки присутсвует на странице и текст ошибки соотносится с ее причиной
        assert incorrect_password_error.is_displayed()
        assert "Некорректный пароль" in incorrect_password_error.text
