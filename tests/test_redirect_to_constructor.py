from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import main_url, account_url
from used_locators import Locators as loc


class TestRedirectToConstructorByClick:
    #  Проверка перехода из личного кабинета в конструктор по клику на «Конструктор»
    def test_redirect_to_constructor_by_click(self, user_logged_driver):

        # Кликнем на «Личный кабинет» на главной странице
        user_logged_driver.find_element(*loc.account_btn_main).click()

        # Добавляем явное ожидание, что страница личного кабинета загрузилась
        WebDriverWait(user_logged_driver, 10).until(EC.url_to_be(account_url))

        # Кликнем на раздел «Конструктор» на странице личного кабинета
        user_logged_driver.find_element(*loc.constructor_header_section).click()

        # Добавим явное ожидание, что кнопка "Оформить заказ" загрузилась на главной странице
        WebDriverWait(user_logged_driver, 10).until(
            EC.visibility_of_element_located((loc.place_order_btn))
        )

        # Находим элемент выбранного раздела на главной странице
        section_active = user_logged_driver.find_element(
            *loc.active_header_section_title
        )

        # Проверяем, что URL текущей страницы совпадает с main_url и выбранный
        # на главной странице раздел соответствует разделу «Конструктор»
        assert user_logged_driver.current_url == main_url
        assert section_active.text == "Конструктор"


class TestRedirectToConstructorByLogoClick:
    #  Проверка перехода из личного кабинета в конструктор по клику на логотип Stellar Burgers
    def test_redirect_to_constructor_by_logo_click(self, user_logged_driver):

        # Кликнем на «Личный кабинет» на главной странице
        user_logged_driver.find_element(*loc.account_btn_main).click()

        # Добавляем явное ожидание, что страница личного кабинета загрузилась
        WebDriverWait(user_logged_driver, 10).until(EC.url_to_be(account_url))

        # Кликнем на логотип Stellar Burgers на странице личного кабинета
        user_logged_driver.find_element(*loc.another_page_logo).click()

        # Добавим явное ожидание, что кнопка "Оформить заказ" загрузилась на главной странице
        WebDriverWait(user_logged_driver, 10).until(
            EC.visibility_of_element_located((loc.place_order_btn))
        )

        # Находим элемент выбранного раздела на главной странице
        section_active = user_logged_driver.find_element(
            *loc.active_header_section_title
        )

        # Проверяем, что URL текущей страницы совпадает с main_url и выбранный
        # на главной странице раздел соответствует разделу «Конструктор»
        assert user_logged_driver.current_url == main_url
        assert section_active.text == "Конструктор"
