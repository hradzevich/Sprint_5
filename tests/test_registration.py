from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import register_url, login_url
from used_locators import Locators as loc
import random as r


class TestRegistrationSuccess:
    # Проверка регистрации нового пользователя с валидными логином(email в формате логин@домен)
    # и паролем(длина более 6 символов)
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

        # Добавляем явное ожидание, что кнопка "Восстановить пароль" загрузилась на странице логина
        WebDriverWait(chrome_driver, 10).until(
            EC.visibility_of_element_located((loc.reset_password_btn))
        )

        # Найдем элемент названия формы логина
        header_login_form = chrome_driver.find_element(*loc.login_form_header)

        # Проверяем, что URL текущей страницы соответствует login_url и название формы для логина "Вход" есть на странице
        assert chrome_driver.current_url == login_url
        assert header_login_form.text == "Вход"


class TestRegistrationInvalidPasswordError:
    # Проверка появления ошибки при регистрации нового пользователя с валидными логином(email в формате логин@домен)
    # и паролем, длина которого менее 6 символов
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

        # Находим элемент с сообщением об ошибке при некорректном пароле
        incorrect_password_error = chrome_driver.find_element(
            *loc.password_error_message
        )

        # Проверяем, что элемент ошибки присутсвует на странице и
        # URL текущей страницы соответствует register_url(не изменился)
        assert chrome_driver.current_url == register_url
        assert "Некорректный пароль" in incorrect_password_error.text
