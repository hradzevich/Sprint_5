from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data.urls import *
from used_locators import Locators as loc
from data.registered_user_data import RegisteredUser


class TestLogin:
    # Проверка входа с главной страницы по кнопке «Войти в аккаунт»
    def test_login_from_main_page_via_login_button(self, chrome_driver):

        # Откроем главную страницу в окне браузера
        chrome_driver.get(MAIN_PAGE)

        # Кликнем на "Войти в аккаунт" на главной странице
        chrome_driver.find_element(*loc.GO_TO_ACCOUNT_MAIN_PAGE_BTN).click()

        # Ждём, что URL изменился на страницу логина
        WebDriverWait(chrome_driver, 10).until(EC.url_to_be(LOGIN_PAGE))

        # Введем в поле "Еmail" значение email пользователя
        chrome_driver.find_element(*loc.FIELD_EMAIL).send_keys(RegisteredUser.email)

        # Введем в поле "Пароль" значение пароля пользователя
        chrome_driver.find_element(*loc.FIELD_PASSWORD).send_keys(
            RegisteredUser.password
        )

        # Добавим явное ожидание, что кнопка "Войти" кликабельна, и кликнем
        WebDriverWait(chrome_driver, 5).until(
            EC.element_to_be_clickable((*loc.LOGIN_BTN,))
        ).click()

        # Добавим явное ожидание, что отображается элемент логотипа, имеющий атрибут aria-current='page'
        WebDriverWait(chrome_driver, 10).until(
            EC.presence_of_element_located((loc.MAIN_PAGE_LOGO))
        )

        # Находим кнопку "Оформить заказ"
        place_order_button = chrome_driver.find_element(*loc.PLACE_ORDER_BTN)

        # Проверяем, что URL главной страницы и кнопка "Оформить заказ", доступная только авторизованным
        # пользователям, отображается на странице
        assert chrome_driver.current_url == MAIN_PAGE
        assert place_order_button.is_displayed()

    # Проверка входа с главной страницы через кнопку «Личный кабинет»
    def test_login_from_main_via_account_button(self, chrome_driver):

        # Откроем главную страницу в окне браузера
        chrome_driver.get(MAIN_PAGE)

        # Кликнем на «Личный кабинет» на главной странице
        chrome_driver.find_element(*loc.ACCOUNT_HEADER_SECTION).click()

        # Ждём, что URL изменился на страницу логина
        WebDriverWait(chrome_driver, 10).until(EC.url_to_be(LOGIN_PAGE))

        # Введем в поле "Еmail" значение email пользователя
        chrome_driver.find_element(*loc.FIELD_EMAIL).send_keys(RegisteredUser.email)

        # Введем в поле "Пароль" значение пароля пользователя
        chrome_driver.find_element(*loc.FIELD_PASSWORD).send_keys(
            RegisteredUser.password
        )

        # Добавим явное ожидание, что кнопка "Войти" кликабельна, и кликнем
        WebDriverWait(chrome_driver, 5).until(
            EC.element_to_be_clickable((*loc.LOGIN_BTN,))
        ).click()

        # Добавим явное ожидание, что отображается элемент логотипа, имеющий атрибут aria-current='page'
        WebDriverWait(chrome_driver, 10).until(
            EC.presence_of_element_located((loc.MAIN_PAGE_LOGO))
        )

        # Находим кнопку "Оформить заказ"
        place_order_button = chrome_driver.find_element(*loc.PLACE_ORDER_BTN)

        # Проверяем, что URL главной страницы и кнопка "Оформить заказ", доступная только авторизованным
        # пользователям, отображается на странице
        assert chrome_driver.current_url == MAIN_PAGE
        assert place_order_button.is_displayed()

    # Проверка входа через кнопку "Войти" в форме регистрации
    def test_login_from_registration(self, chrome_driver):

        # Откроем страницу регистрации в окне браузера
        chrome_driver.get(REGISTRATION_PAGE)

        # Кликнем на кнопку "Войти" на странице регистрации
        chrome_driver.find_element(*loc.LOGIN_BTN_REGISTRATION).click()

        # Ждём, что URL изменился на страницу логина
        WebDriverWait(chrome_driver, 10).until(EC.url_to_be(LOGIN_PAGE))

        # Введем в поле "Еmail" значение email пользователя
        chrome_driver.find_element(*loc.FIELD_EMAIL).send_keys(RegisteredUser.email)

        # Введем в поле "Пароль" значение пароля пользователя
        chrome_driver.find_element(*loc.FIELD_PASSWORD).send_keys(
            RegisteredUser.password
        )

        # Добавим явное ожидание, что кнопка "Войти" кликабельна, и кликнем
        WebDriverWait(chrome_driver, 5).until(
            EC.element_to_be_clickable((*loc.LOGIN_BTN,))
        ).click()

        # Добавим явное ожидание, что отображается элемент логотипа, имеющий атрибут aria-current='page'
        WebDriverWait(chrome_driver, 10).until(
            EC.presence_of_element_located((loc.MAIN_PAGE_LOGO))
        )

        # Находим кнопку "Оформить заказ"
        place_order_button = chrome_driver.find_element(*loc.PLACE_ORDER_BTN)

        # Проверяем, что URL главной страницы и кнопка "Оформить заказ", доступная только авторизованным
        # пользователям, отображается на странице
        assert chrome_driver.current_url == MAIN_PAGE
        assert place_order_button.is_displayed()

    # Проверка входа через кнопку в форме восстановления пароля
    def test_login_via_password_reset(self, chrome_driver):

        # Откроем страницу восстановления пароля в окне браузера
        chrome_driver.get(RESET_PASSWORD_PAGE)

        # Кликнем на кнопку "Войти" на странице восстановления пароля
        chrome_driver.find_element(*loc.LOGIN_BTN_RESET_PASSWORD).click()

        # Ждём, что URL изменился на страницу логина
        WebDriverWait(chrome_driver, 10).until(EC.url_to_be(LOGIN_PAGE))

        # Введем в поле "Еmail" значение email пользователя
        chrome_driver.find_element(*loc.FIELD_EMAIL).send_keys(RegisteredUser.email)

        # Введем в поле "Пароль" значение пароля пользователя
        chrome_driver.find_element(*loc.FIELD_PASSWORD).send_keys(
            RegisteredUser.password
        )

        # Добавим явное ожидание, что кнопка "Войти" кликабельна, и кликнем
        WebDriverWait(chrome_driver, 5).until(
            EC.element_to_be_clickable((*loc.LOGIN_BTN,))
        ).click()

        # Добавим явное ожидание, что отображается элемент логотипа, имеющий атрибут aria-current='page'
        WebDriverWait(chrome_driver, 10).until(
            EC.presence_of_element_located((loc.MAIN_PAGE_LOGO))
        )

        # Находим кнопку "Оформить заказ"
        place_order_button = chrome_driver.find_element(*loc.PLACE_ORDER_BTN)

        # Проверяем, что URL главной страницы и кнопка "Оформить заказ", доступная только авторизованным
        # пользователям, отображается на странице
        assert chrome_driver.current_url == MAIN_PAGE
        assert place_order_button.is_displayed()
