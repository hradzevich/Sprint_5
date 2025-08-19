from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data.urls import REGISTRATION_PAGE, LOGIN_PAGE
from used_locators import Locators as loc
import random as r
from data.generation_user_data import generate_user_data


class TestRegistrationSuccess:
    # Проверка регистрации нового пользователя с валидными логином(email в формате логин@домен)
    # и паролем(длина более 6 символов)
    def test_registration_valid_credentials_success(self, chrome_driver):
        # Вызываем метод для генерации тестовых данных пользователя
        name, email, password = generate_user_data()

        # Откроем страницу регистрации в окне браузера
        chrome_driver.get(REGISTRATION_PAGE)

        # Введем в поле "Имя" значение имени пользователя
        chrome_driver.find_element(*loc.FIELD_NAME).send_keys(name)

        # Введем в поле "Еmail" значение email пользователя
        chrome_driver.find_element(*loc.FIELD_EMAIL).send_keys(email)

        # Введем в поле "Пароль" значение пароля пользователя
        chrome_driver.find_element(*loc.FIELD_PASSWORD).send_keys(password)

        # Кликнем на кнопку "Зарегистрироваться"
        chrome_driver.find_element(*loc.REGISTRATION_BTN).click()

        # Добавляем явное ожидание, что кнопка "Восстановить пароль" загрузилась на странице логина
        WebDriverWait(chrome_driver, 10).until(
            EC.visibility_of_element_located((loc.RESET_PASSWORD_BTN))
        )

        # Найдем элемент названия формы логина
        header_login_form = chrome_driver.find_element(*loc.LOGIN_FORM_TITLE)

        # Проверяем, что URL текущей страницы соответствует LOGIN_PAGE и название формы для логина "Вход" есть на странице
        assert chrome_driver.current_url == LOGIN_PAGE
        assert header_login_form.text == "Вход"


class TestRegistrationInvalidPasswordError:
    # Проверка появления ошибки при регистрации нового пользователя с валидными логином(email в формате логин@домен)
    # и паролем, длина которого менее 6 символов
    def test_registration_invalid_password_error(self, chrome_driver):
        # Вызываем метод для генерации тестовых данных пользователя
        name, email, _ = generate_user_data()

        # Откроем страницу регистрации в окне браузера
        chrome_driver.get(REGISTRATION_PAGE)

        # Введем в поле "Имя" значение имени пользователя
        chrome_driver.find_element(*loc.FIELD_NAME).send_keys(name)

        # Введем в поле "Еmail" значение email пользователя
        chrome_driver.find_element(*loc.FIELD_EMAIL).send_keys(email)

        # Сгенерируем переменную password с невалидным значением пароля пользователя (длина 5 символов)
        numbers_plus_letters = "1234567890abcdefghijklmnopqrstuvwxyz"
        password = "".join(r.sample(numbers_plus_letters, 5))

        # Введем в поле "Пароль" значение пароля пользователя
        chrome_driver.find_element(*loc.FIELD_PASSWORD).send_keys(password)

        # Кликнем на кнопку "Зарегистрироваться", чтобы снять фокус с поля "Пароль"
        chrome_driver.find_element(*loc.REGISTRATION_BTN).click()

        # Находим элемент с сообщением об ошибке при некорректном пароле
        incorrect_password_error = chrome_driver.find_element(
            *loc.PASSWORD_ERROR_MESSAGE
        )

        # Проверяем, что элемент ошибки присутсвует на странице и
        # URL текущей страницы соответствует REGISTRATION_PAGE(не изменился)
        assert chrome_driver.current_url == REGISTRATION_PAGE
        assert "Некорректный пароль" in incorrect_password_error.text
