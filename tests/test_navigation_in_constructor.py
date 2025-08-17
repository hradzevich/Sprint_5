from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import main_url
from used_locators import Locators as loc


class TestNavigationInConstructoToSauces:
    # Проверка работы переходов к разделу «Соусы»
    def test_navigation_in_constructor_to_sauces(self, chrome_driver):

        # Откроем главную страницу  в окне браузера
        chrome_driver.get(main_url)

        # Добавим явное ожидание, что выбран раздел "Конструктор"(атрибут aria-current="page")
        WebDriverWait(chrome_driver, 10).until(
            EC.text_to_be_present_in_element_attribute(
                loc.constructor_header_section, "aria-current", "page"
            )
        )

        # Кликнем на подраздел "Соусы"
        chrome_driver.find_element(*loc.constructor_section_sauces).click()

        # Находим элемент выбранного подраздела в разделе "Конструктора"
        selected_section = chrome_driver.find_element(*loc.constructor_section_active)

        # Проверяем, что выбран подраздел "Соусы"
        assert selected_section.text == "Соусы"


class TestNavigationInConstructorToFillings:
    # Проверка работы переходов к разделу «Начинки»
    def test_navigation_in_constructor_to_fillings(self, chrome_driver):

        # Откроем главную страницу  в окне браузера
        chrome_driver.get(main_url)

        # Добавим явное ожидание, что выбран раздел "Конструктор"(атрибут aria-current="page")
        WebDriverWait(chrome_driver, 10).until(
            EC.text_to_be_present_in_element_attribute(
                loc.constructor_header_section, "aria-current", "page"
            )
        )

        # Кликнем на подраздел "Начинки"
        chrome_driver.find_element(*loc.constructor_section_fillings).click()

        # Находим элемент выбранного подраздела в разделе "Конструктора"
        selected_section = chrome_driver.find_element(*loc.constructor_section_active)

        # Проверяем, что выбран подраздел "Начинки"
        assert selected_section.text == "Начинки"


class TestNavigationInConstructorToBuns:
    # Проверка работы переходов к разделу «Булки»
    def test_navigation_in_constructor_to_buns(self, chrome_driver):

        # Откроем главную страницу  в окне браузера
        chrome_driver.get(main_url)

        # Добавим явное ожидание, что выбран раздел "Конструктор"(атрибут aria-current="page")
        WebDriverWait(chrome_driver, 10).until(
            EC.text_to_be_present_in_element_attribute(
                loc.constructor_header_section, "aria-current", "page"
            )
        )

        # Кликнем на подраздел "Начинки", чтобы сменить выбранный подраздел
        chrome_driver.find_element(*loc.constructor_section_fillings).click()

        # Кликнем на подраздел "Булки"
        chrome_driver.find_element(*loc.constructor_section_buns).click()

        # Находим элемент выбранного подраздела в разделе "Конструктора"
        selected_section = chrome_driver.find_element(*loc.constructor_section_active)

        # Проверяем, что выбран подраздел "Булки"
        assert selected_section.text == "Булки"
