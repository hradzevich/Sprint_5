from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import login_url
from used_locators import Locators as loc


class TestLogoutFromAccount:
    #  Проверка выхода по кнопке «Выход» в личном кабинете
    def test_logout_from_account_by_logout_btn_click(self, user_logged_driver):

        # Кликнем на «Личный кабинет» на главной странице
        user_logged_driver.find_element(*loc.account_btn_main).click()

        # Добавляем явное ожидание, что кнопкa "Выход" отображается на странице личного кабинета
        WebDriverWait(user_logged_driver, 10).until(
            EC.visibility_of_element_located((loc.logout_btn_account_page))
        )

        # Кликнем на кнопку "Выход" на странице личного кабинета
        user_logged_driver.find_element(*loc.logout_btn_account_page).click()

        # Ждём, что URL изменился на страницу логина
        WebDriverWait(user_logged_driver, 10).until(EC.url_to_be(login_url))

        # Найдем элемент названия формы логина
        login_form_header = user_logged_driver.find_element(*loc.login_form_header)

        # Проверяем, что URL текущей страницы соответствует login_url и название формы для логина "Вход" есть на странице
        assert user_logged_driver.current_url == login_url
        assert login_form_header.text == "Вход"
