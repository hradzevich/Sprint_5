from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import register_url, main_url, login_url
from used_locators import Locators as loc


class TestRegistrationSuccess:
    # Проверка регистрации нового пользователя с валидными логином(email в формате логин@домен) и паролем(длина болеее 6 символов)
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

        # Ждём, что URL изменился на страницу логина
        WebDriverWait(chrome_driver, 10).until(EC.url_to_be(login_url))

        # Введем в поле "Еmail" значение email пользователя
        chrome_driver.find_element(*loc.field_email).send_keys(email)

        # Введем в поле "Пароль" значение пароля пользователя
        chrome_driver.find_element(*loc.field_password).send_keys(password)

        # Добавим явное ожидание, что кнопка кликабельна
        WebDriverWait(chrome_driver, 5).until(
            EC.element_to_be_clickable((*loc.login_btn,))
        )

        # Кликнем на кнопку "Войти"
        chrome_driver.find_element(*loc.login_btn).click()

        # Добавим явное ожидание, что кнопка "Оформить заказ" загрузилась на странице
        WebDriverWait(chrome_driver, 10).until(
            EC.visibility_of_element_located((loc.place_order_btn))
        )

        # Проверка, что на странице присутсвует кнопка с текстом "Оформить заказ" вместо "Войти в аккаунт"
        assert chrome_driver.find_element(*loc.place_order_btn).text == "Оформить заказ"
