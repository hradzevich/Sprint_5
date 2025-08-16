from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import main_url
from used_locators import Locators as loc


class TestRedirectToConstructorByClick:
    #  Проверка перехода из личного кабинета в конструктор по клику на «Конструктор»
    def test_redirect_to_constructor_by_click(self, user_logged_driver):

        # Кликнем на «Личный кабинет» на главной странице
        user_logged_driver.find_element(*loc.account_btn_main).click()

        # Добавляем явное ожидание, что название раздела «Личный кабинет» загрузилось
        WebDriverWait(user_logged_driver, 10).until(
            EC.visibility_of_element_located((loc.account_page_title))
        )

        # Кликнем на раздел «Конструктор» на стринице личного кабинета
        user_logged_driver.find_element(*loc.account_page_constructor_section).click()

        # Добавим явное ожидание, что кнопка "Оформить заказ" загрузилась на главной странице
        WebDriverWait(user_logged_driver, 10).until(
            EC.visibility_of_element_located((loc.place_order_btn))
        )

        # Находим элемент с заголовком раздела «Конструктор» на главной странице
        constructor_section_active = user_logged_driver.find_element(
            *loc.constructor_section_main_page
        )

        # Проверяем, что URL текущей страницы совпадает с main_url и раздел «Конструктор» на главной странице активный
        assert user_logged_driver.current_url == main_url
        assert constructor_section_active.get_attribute("aria-current") == "page"


class TestRedirectToConstructorByLogoClick:
    #  Проверка перехода из личного кабинета в конструктор по клику на логотип Stellar Burgers
    def test_redirect_to_constructor_by__logo_click(self, user_logged_driver):

        # Кликнем на «Личный кабинет» на главной странице
        user_logged_driver.find_element(*loc.account_btn_main).click()

        # Добавляем явное ожидание, что название раздела «Личный кабинет» загрузилось
        WebDriverWait(user_logged_driver, 10).until(
            EC.visibility_of_element_located((loc.account_page_title))
        )

        # Кликнем на логотип Stellar Burgers на стринице личного кабинета
        user_logged_driver.find_element(*loc.account_page_logo).click()

        # Добавим явное ожидание, что кнопка "Оформить заказ" загрузилась на главной странице
        WebDriverWait(user_logged_driver, 10).until(
            EC.visibility_of_element_located((loc.place_order_btn))
        )

        # Находим элемент с заголовком раздела «Конструктор» на главной странице
        constructor_section_active = user_logged_driver.find_element(
            *loc.constructor_section_main_page
        )

        # Проверяем, что URL текущей страницы совпадает с main_url и раздел «Конструктор» на главной странице активный
        assert user_logged_driver.current_url == main_url
        assert constructor_section_active.get_attribute("aria-current") == "page"
