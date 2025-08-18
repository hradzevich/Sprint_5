from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import MAIN_PAGE, ACCOUNT_PAGE
from used_locators import Locators as loc


class TestRedirectToConstructorByClick:
    #  Проверка перехода из личного кабинета в конструктор по клику на «Конструктор»
    def test_redirect_to_constructor_by_click(self, user_logged_driver):

        # Кликнем на «Личный кабинет» на главной странице
        user_logged_driver.find_element(*loc.ACCOUNT_HEADER_SECTION).click()

        # Добавляем явное ожидание, что страница личного кабинета загрузилась
        WebDriverWait(user_logged_driver, 10).until(EC.url_to_be(ACCOUNT_PAGE))

        # Кликнем на раздел «Конструктор» на странице личного кабинета
        user_logged_driver.find_element(*loc.CONSTRACTOR_HEADER_SECTION).click()

        # Добавим явное ожидание, что кнопка "Оформить заказ" загрузилась на главной странице
        WebDriverWait(user_logged_driver, 10).until(
            EC.visibility_of_element_located((loc.PLACE_ORDER_BTN))
        )

        # Находим элемент выбранного раздела на главной странице
        section_active = user_logged_driver.find_element(
            *loc.ACTIVE_SECTION_HEADER_TITLE
        )

        # Проверяем, что URL текущей страницы совпадает с MAIN_PAGE и выбранный
        # на главной странице раздел соответствует разделу «Конструктор»
        assert user_logged_driver.current_url == MAIN_PAGE
        assert section_active.text == "Конструктор"


class TestRedirectToConstructorByLogoClick:
    #  Проверка перехода из личного кабинета в конструктор по клику на логотип Stellar Burgers
    def test_redirect_to_constructor_by_logo_click(self, user_logged_driver):

        # Кликнем на «Личный кабинет» на главной странице
        user_logged_driver.find_element(*loc.ACCOUNT_HEADER_SECTION).click()

        # Добавляем явное ожидание, что страница личного кабинета загрузилась
        WebDriverWait(user_logged_driver, 10).until(EC.url_to_be(ACCOUNT_PAGE))

        # Кликнем на логотип Stellar Burgers на странице личного кабинета
        user_logged_driver.find_element(*loc.NOT_MAIN_PAGE_LOGO).click()

        # Добавим явное ожидание, что кнопка "Оформить заказ" загрузилась на главной странице
        WebDriverWait(user_logged_driver, 10).until(
            EC.visibility_of_element_located((loc.PLACE_ORDER_BTN))
        )

        # Находим элемент выбранного раздела на главной странице
        section_active = user_logged_driver.find_element(
            *loc.ACTIVE_SECTION_HEADER_TITLE
        )

        # Проверяем, что URL текущей страницы совпадает с MAIN_PAGE и выбранный
        # на главной странице раздел соответствует разделу «Конструктор»
        assert user_logged_driver.current_url == MAIN_PAGE
        assert section_active.text == "Конструктор"
