from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import main_url
from used_locators import Locators as loc


class TestNavigationInConstructorBunsDefault:
    # Проверка работы переходов, раздел «Булки» активный по умолчанию
    def test_navigation_in_constructor_buns_default(self, chrome_driver):

        # Откроем главную страницу  в окне браузера
        chrome_driver.get(main_url)

        # Добавим явное ожидание, что отображается элемент логотипа, имеющий атрибут aria-current='page'
        WebDriverWait(chrome_driver, 10).until(
            EC.presence_of_element_located((loc.main_page_logo))
        )
        # Находим элемент выбранного по умолчанию раздела "Конструктора"
        default_section = chrome_driver.find_element(*loc.constructor_section_active)

        # Проверяем, что по умолчанию выбран раздел "Булки"
        assert default_section.text == "Булки"


class TestNavigationInConstructoToSauces:
    # Проверка работы переходов к разделу «Соусы»
    def test_navigation_in_constructor_to_sauces(self, chrome_driver):

        # Откроем главную страницу  в окне браузера
        chrome_driver.get(main_url)

        # Добавим явное ожидание, что отображается элемент логотипа, имеющий атрибут aria-current='page'
        WebDriverWait(chrome_driver, 10).until(
            EC.presence_of_element_located((loc.main_page_logo))
        )

        # Кликнем на подраздел "Соусы"
        chrome_driver.find_element(*loc.constructor_section_sauces).click()

        # Находим элемент выбранного по подраздела "Соусы" в разделе "Конструктора"
        selected_section = chrome_driver.find_element(*loc.constructor_section_active)

        # Проверяем, что выбран подраздел "Соусы"
        assert selected_section.text == "Соусы"


class TestNavigationInConstructorToFillings:
    # Проверка работы переходов к разделу «Начинки»
    def test_navigation_in_constructor_to_fillings(self, chrome_driver):

        # Откроем главную страницу  в окне браузера
        chrome_driver.get(main_url)

        # Добавим явное ожидание, что отображается элемент логотипа, имеющий атрибут aria-current='page'
        WebDriverWait(chrome_driver, 10).until(
            EC.presence_of_element_located((loc.main_page_logo))
        )

        # Кликнем на подраздел "Начинки"
        chrome_driver.find_element(*loc.constructor_section_fillings).click()

        # Находим элемент выбранного по подраздела "Начинки" в разделе "Конструктора"
        selected_section = chrome_driver.find_element(*loc.constructor_section_active)

        # Проверяем, что выбран подраздел "Начинки"
        assert selected_section.text == "Начинки"


class TestNavigationInConstructorToBuns:
    # Проверка работы переходов к разделу «Булки»
    def test_navigation_in_constructor_to_buns(self, chrome_driver):

        # Откроем главную страницу  в окне браузера
        chrome_driver.get(main_url)

        # Добавим явное ожидание, что отображается элемент логотипа, имеющий атрибут aria-current='page'
        WebDriverWait(chrome_driver, 10).until(
            EC.presence_of_element_located((loc.main_page_logo))
        )

        # Кликнем на подраздел "Начинки", чтобы сменить выбранный подраздел
        chrome_driver.find_element(*loc.constructor_section_fillings).click()

        # Кликнем на подраздел "Булки"
        chrome_driver.find_element(*loc.constructor_section_buns).click()

        # Находим элемент выбранного по подраздела "Булки" в разделе "Конструктора"
        selected_section = chrome_driver.find_element(*loc.constructor_section_active)

        # Проверяем, что выбран подраздел "Булки"
        assert selected_section.text == "Булки"
