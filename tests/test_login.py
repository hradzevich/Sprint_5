from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import main_url, login_url, register_url, reset_password_url
from used_locators import Locators as loc


class TestLoginViaLoginButton:
    # Проверка входа с главной страницы по кнопке «Войти в аккаунт»
    def test_login_from_main_page_via_login_button(
        self, chrome_driver, registered_user
    ):

        # Откроем главную страницу в окне браузера
        chrome_driver.get(main_url)

        # Кликнем на "Войти в аккаунт" на главной странице
        chrome_driver.find_element(*loc.go_to_account_main_btn).click()

        # Ждём, что URL изменился на страницу логина
        WebDriverWait(chrome_driver, 10).until(EC.url_to_be(login_url))

        # Введем в поле "Еmail" значение email пользователя
        chrome_driver.find_element(*loc.field_email).send_keys(registered_user["email"])

        # Введем в поле "Пароль" значение пароля пользователя
        chrome_driver.find_element(*loc.field_password).send_keys(
            registered_user["password"]
        )

        # Добавим явное ожидание, что кнопка "Войти" кликабельна
        WebDriverWait(chrome_driver, 5).until(
            EC.element_to_be_clickable((*loc.login_btn,))
        )

        # Кликнем на кнопку "Войти"
        chrome_driver.find_element(*loc.login_btn).click()

        # Добавим явное ожидание, что кнопка "Оформить заказ", доступная только авторизованным пользователям, загрузилась на странице
        WebDriverWait(chrome_driver, 10).until(
            EC.visibility_of_element_located((loc.place_order_btn))
        )

        # Проверяем, что открылся URL главной страницы
        assert chrome_driver.current_url == main_url


class TestLoginViaAccountButton:
    # Проверка входа с главной страницы через кнопку «Личный кабинет»
    def test_login_from_main_via_account_button(self, chrome_driver, registered_user):

        # Откроем главную страницу в окне браузера
        chrome_driver.get(main_url)

        # Кликнем на «Личный кабинет» на главной странице
        chrome_driver.find_element(*loc.account_btn_main).click()

        # Ждём, что URL изменился на страницу логина
        WebDriverWait(chrome_driver, 10).until(EC.url_to_be(login_url))

        # Введем в поле "Еmail" значение email пользователя
        chrome_driver.find_element(*loc.field_email).send_keys(registered_user["email"])

        # Введем в поле "Пароль" значение пароля пользователя
        chrome_driver.find_element(*loc.field_password).send_keys(
            registered_user["password"]
        )

        # Добавим явное ожидание, что кнопка "Войти" кликабельна
        WebDriverWait(chrome_driver, 5).until(
            EC.element_to_be_clickable((*loc.login_btn,))
        )

        # Кликнем на кнопку "Войти"
        chrome_driver.find_element(*loc.login_btn).click()

        # Добавим явное ожидание, что кнопка "Оформить заказ", доступная только авторизованным пользователям, загрузилась на странице
        WebDriverWait(chrome_driver, 10).until(
            EC.visibility_of_element_located((loc.place_order_btn))
        )

        # Проверяем, что открылся URL главной страницы
        assert chrome_driver.current_url == main_url


class TestLoginViaRegistration:
    # Проверка входа через кнопку "Войти" в форме регистрации
    def test_login_from_registration(self, chrome_driver, registered_user):

        # Откроем страницу регистрации в окне браузера
        chrome_driver.get(register_url)

        # Кликнем на кнопку "Войти" на странице регистрации
        chrome_driver.find_element(*loc.login_btn_registration).click()

        # Ждём, что URL изменился на страницу логина
        WebDriverWait(chrome_driver, 10).until(EC.url_to_be(login_url))

        # Введем в поле "Еmail" значение email пользователя
        chrome_driver.find_element(*loc.field_email).send_keys(registered_user["email"])

        # Введем в поле "Пароль" значение пароля пользователя
        chrome_driver.find_element(*loc.field_password).send_keys(
            registered_user["password"]
        )

        # Добавим явное ожидание, что кнопка "Войти" кликабельна
        WebDriverWait(chrome_driver, 5).until(
            EC.element_to_be_clickable((*loc.login_btn,))
        )

        # Кликнем на кнопку "Войти"
        chrome_driver.find_element(*loc.login_btn).click()

        # Добавим явное ожидание, что кнопка "Оформить заказ", доступная только авторизованным пользователям, загрузилась на странице
        WebDriverWait(chrome_driver, 10).until(
            EC.visibility_of_element_located((loc.place_order_btn))
        )

        # Проверяем, что открылся URL главной страницы
        assert chrome_driver.current_url == main_url


class TestLoginViaPasswordReset:
    # Проверка входа через кнопку в форме восстановления пароля
    def test_login_via_password_reset(self, chrome_driver, registered_user):

        # Откроем страницу восстановления пароля в окне браузера
        chrome_driver.get(reset_password_url)

        # Кликнем на кнопку "Войти" на странице восстановления пароля
        chrome_driver.find_element(*loc.login_btn_rest_password).click()

        # Ждём, что URL изменился на страницу логина
        WebDriverWait(chrome_driver, 10).until(EC.url_to_be(login_url))

        # Введем в поле "Еmail" значение email пользователя
        chrome_driver.find_element(*loc.field_email).send_keys(registered_user["email"])

        # Введем в поле "Пароль" значение пароля пользователя
        chrome_driver.find_element(*loc.field_password).send_keys(
            registered_user["password"]
        )

        # Добавим явное ожидание, что кнопка "Войти" кликабельна
        WebDriverWait(chrome_driver, 5).until(
            EC.element_to_be_clickable((*loc.login_btn,))
        )

        # Кликнем на кнопку "Войти"
        chrome_driver.find_element(*loc.login_btn).click()

        # Добавим явное ожидание, что кнопка "Оформить заказ", доступная только авторизованным пользователям, загрузилась на странице
        WebDriverWait(chrome_driver, 10).until(
            EC.visibility_of_element_located((loc.place_order_btn))
        )

        # Проверяем, что открылся URL главной страницы
        assert chrome_driver.current_url == main_url
