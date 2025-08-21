import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data.urls import MAIN_PAGE
from used_locators import Locators as loc
from data.texts_data import *


class TestNavigationInConstructor:
    # Параметризация переходов между разделами конструктора:
    # start_locator / start_title — с какого раздела начинаем
    # target_locator / target_title — в какой раздел переходим и что ожидаем
    @pytest.mark.parametrize(
        "start_locator, start_title, target_locator, target_title",
        [
            # Начинки -> Соусы
            (
                loc.CONSTRUCTOR_SUBSECTION_FILLINGS,
                CONSTRUCTOR_SECTION_FILLINGS_TITLE,
                loc.CONSTRUCTOR_SUBSECTION_SAUCES,
                CONSTRUCTOR_SECTION_SAUCES_TITLE,
            ),
            # Соусы -> Начинки
            (
                loc.CONSTRUCTOR_SUBSECTION_SAUCES,
                CONSTRUCTOR_SECTION_SAUCES_TITLE,
                loc.CONSTRUCTOR_SUBSECTION_FILLINGS,
                CONSTRUCTOR_SECTION_FILLINGS_TITLE,
            ),
            # Соусы -> Булки
            (
                loc.CONSTRUCTOR_SUBSECTION_SAUCES,
                CONSTRUCTOR_SECTION_SAUCES_TITLE,
                loc.CONSTRUCTOR_SUBSECTION_BUNS,
                CONSTRUCTOR_SECTION_BUNS_TITLE,
            ),
        ],
    )
    # Проверка работы переходов к target разделу
    def test_navigation_in_constructor(
        self, chrome_driver, start_locator, start_title, target_locator, target_title
    ):

        # Откроем главную страницу  в окне браузера
        chrome_driver.get(MAIN_PAGE)

        # Добавим явное ожидание, что выбран раздел "Конструктор"(атрибут aria-current="page")
        WebDriverWait(chrome_driver, 10).until(
            EC.text_to_be_present_in_element_attribute(
                loc.CONSTRACTOR_HEADER_SECTION, "aria-current", "page"
            )
        )

        # Кликнем на любой подраздел, чтобы сменить текущий подраздел(по умолчанию "Булки")
        WebDriverWait(chrome_driver, 10).until(
            EC.element_to_be_clickable(start_locator)
        ).click()

        # Добавим явное ожидание, что подраздел "Булки" сменился на выбранный подраздел 
        WebDriverWait(chrome_driver, 10).until(
            EC.text_to_be_present_in_element(
                loc.CONSTRUCTOR_ACTIVE_SUBSECTION, start_title
            )
        )

        # Кликнем на target подраздел
        chrome_driver.find_element(*target_locator).click()

        # Находим элемент выбранного подраздела в разделе "Конструктора"
        selected_section = chrome_driver.find_element(
            *loc.CONSTRUCTOR_ACTIVE_SUBSECTION
        )

        # Проверяем, что выбран target подраздел
        assert selected_section.text == target_title
