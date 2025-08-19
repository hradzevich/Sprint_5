from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data.urls import MAIN_PAGE
from used_locators import Locators as loc


class TestNavigationInConstructor:
    # Проверка работы переходов к разделу «Соусы»
    def test_navigation_in_constructor_to_sauces(self, chrome_driver):

        # Откроем главную страницу  в окне браузера
        chrome_driver.get(MAIN_PAGE)

        # Добавим явное ожидание, что выбран раздел "Конструктор"(атрибут aria-current="page")
        WebDriverWait(chrome_driver, 10).until(
            EC.text_to_be_present_in_element_attribute(
                loc.CONSTRACTOR_HEADER_SECTION, "aria-current", "page"
            )
        )

        # Кликнем на подраздел "Соусы"
        chrome_driver.find_element(*loc.CONSTRUCTOR_SUBSECTION_SAUCES).click()

        # Находим элемент выбранного подраздела в разделе "Конструктора"
        selected_section = chrome_driver.find_element(
            *loc.CONSTRUCTOR_ACTIVE_SUBSECTION
        )

        # Проверяем, что выбран подраздел "Соусы"
        assert selected_section.text == "Соусы"

    # Проверка работы переходов к разделу «Начинки»
    def test_navigation_in_constructor_to_fillings(self, chrome_driver):

        # Откроем главную страницу  в окне браузера
        chrome_driver.get(MAIN_PAGE)

        # Добавим явное ожидание, что выбран раздел "Конструктор"(атрибут aria-current="page")
        WebDriverWait(chrome_driver, 10).until(
            EC.text_to_be_present_in_element_attribute(
                loc.CONSTRACTOR_HEADER_SECTION, "aria-current", "page"
            )
        )

        # Кликнем на подраздел "Начинки"
        chrome_driver.find_element(*loc.CONSTRUCTOR_SUBSECTION_FILLINGS).click()

        # Находим элемент выбранного подраздела в разделе "Конструктора"
        selected_section = chrome_driver.find_element(
            *loc.CONSTRUCTOR_ACTIVE_SUBSECTION
        )

        # Проверяем, что выбран подраздел "Начинки"
        assert selected_section.text == "Начинки"

    # Проверка работы переходов к разделу «Булки»
    def test_navigation_in_constructor_to_buns(self, chrome_driver):

        # Откроем главную страницу  в окне браузера
        chrome_driver.get(MAIN_PAGE)

        # Добавим явное ожидание, что выбран раздел "Конструктор"(атрибут aria-current="page")
        WebDriverWait(chrome_driver, 10).until(
            EC.text_to_be_present_in_element_attribute(
                loc.CONSTRACTOR_HEADER_SECTION, "aria-current", "page"
            )
        )

        # Кликнем на подраздел "Начинки", чтобы сменить выбранный подраздел
        chrome_driver.find_element(*loc.CONSTRUCTOR_SUBSECTION_FILLINGS).click()

        # Добавим явное ожидание, что подраздел "Булки" сменился на подраздел "Начинки"
        WebDriverWait(chrome_driver, 10).until(
            EC.text_to_be_present_in_element(
                loc.CONSTRUCTOR_ACTIVE_SUBSECTION, "Начинки"
            )
        )

        # Кликнем на подраздел "Булки"
        chrome_driver.find_element(*loc.CONSTRUCTOR_SUBSECTION_BUNS).click()

        # Находим элемент выбранного подраздела в разделе "Конструктора"
        selected_section = chrome_driver.find_element(
            *loc.CONSTRUCTOR_ACTIVE_SUBSECTION
        )

        # Проверяем, что выбран подраздел "Булки"
        assert selected_section.text == "Булки"
