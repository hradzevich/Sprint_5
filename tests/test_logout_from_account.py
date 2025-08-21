from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data.urls import LOGIN_PAGE
from used_locators import Locators as loc
from data.texts_data import *


class TestLogoutFromAccount:
    #  Проверка выхода по кнопке «Выход» в личном кабинете
    def test_logout_from_account_by_logout_btn_click(self, user_logged_driver):

        # Кликнем на «Личный кабинет» на главной странице
        user_logged_driver.find_element(*loc.ACCOUNT_HEADER_SECTION).click()

        # Добавляем явное ожидание, что кнопкa "Выход" отображается на странице личного кабинета, и кликнем
        WebDriverWait(user_logged_driver, 10).until(
            EC.visibility_of_element_located((loc.LOGOUT_BTN))
        ).click()

        # Добавляем явное ожидание, что кнопка "Восстановить пароль" загрузилась на странице логина
        WebDriverWait(user_logged_driver, 10).until(
            EC.visibility_of_element_located((loc.RESET_PASSWORD_BTN))
        )

        # Найдем элемент названия формы логина
        login_form_title = user_logged_driver.find_element(*loc.LOGIN_FORM_TITLE)

        # Проверяем, что URL текущей страницы соответствует LOGIN_PAGE и название формы для логина "Вход" есть на странице
        assert user_logged_driver.current_url == LOGIN_PAGE
        assert login_form_title.text == LOGIN_TITLE
