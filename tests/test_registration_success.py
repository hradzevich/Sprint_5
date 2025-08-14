from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import register_url, main_url
import used_locators as loc


class TestRegistration:
    # Проверка регистрации нового пользователя с валидными логином(email в формате логин@домен) и паролем(длина болеее 6 символов)
    def test_registration_valid_credentials_success(self, chrome_driver, user_data):

        # Откроем страницу регистрации в окне браузера
        chrome_driver.get(register_url)

        # Добавим явное ожидание, что форма регистрации загрузилась
        WebDriverWait(chrome_driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    loc.registration_form,
                )
            )
        )
        # Введем в поле "Имя" значение имени пользователя
        chrome_driver.find_element(By.XPATH, loc.registration_form_name).send_keys(
            user_data["name"]
        )

        # Сохраним в переменную email значение email пользователя, которое далее используем для входа
        email = user_data["login"]

        # Введем в поле "Еmail" значение email пользователя
        chrome_driver.find_element(By.XPATH, loc.registration_form_email).send_keys(
            email
        )

        # Сохраним в переменную password значение пароля пользователя, которое далее используем для входа
        password = user_data["password"]

        # Введем в поле "Пароль" значение пароля пользователя
        chrome_driver.find_element(By.XPATH, loc.registration_form_password).send_keys(
            password
        )

        # Кликнем на кнопку "Зарегистрироваться"
        chrome_driver.find_element(By.XPATH, loc.registration_btn).click()

        # Добавим явное ожидание, что форма для логина загрузилась
        WebDriverWait(chrome_driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    loc.login_form,
                )
            )
        )

        # Введем в поле "Еmail" значение email пользователя
        chrome_driver.find_element(By.XPATH, loc.login_form_email).send_keys(email)

        # Введем в поле "Пароль" значение пароля пользователя
        chrome_driver.find_element(By.XPATH, loc.login_form_password).send_keys(
            password
        )

        # Кликнем на кнопку "Войти"
        chrome_driver.find_element(By.XPATH, loc.login_btn).click()

        # Добавим явное ожидание, что главная страница загрузилась
        WebDriverWait(chrome_driver, 10).until(EC.url_to_be(main_url))

        # Проверка, что на странице присутсвует кнопка "Оформить заказ" вместо "Войти в аккаунт"
        assert (
            chrome_driver.find_element(By.XPATH, loc.place_order_btn).text
            == "Оформить заказ"
        )
