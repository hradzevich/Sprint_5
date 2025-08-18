from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import MAIN_PAGE, ACCOUNT_PAGE
from used_locators import Locators as loc
from registered_user_data import RegisteredUser


class TestRedirectToAccount:
    # Проверка перехода в личный кабинет  по клику на «Личный кабинет».
    def test_redirect_to_account_from_main(self, user_logged_driver):

        # Откроем главную страницу в окне браузера как залогированный пользователь
        user_logged_driver.get(MAIN_PAGE)

        # Кликнем на «Личный кабинет» на главной странице
        user_logged_driver.find_element(*loc.ACCOUNT_HEADER_SECTION).click()

        # Добавляем явное ожидание, что раздел "Личный кабинет" выбран (атрибут aria-current="page")
        WebDriverWait(user_logged_driver, 10).until(
            EC.text_to_be_present_in_element_attribute(
                loc.ACCOUNT_HEADER_SECTION, "aria-current", "page"
            )
        )

        # Добавляем явное ожидание, что форма с данными пользователя (поле "Логин") загрузилась
        WebDriverWait(user_logged_driver, 10).until(
            EC.visibility_of_element_located((loc.ACCOUNT_FIELD_EMAIL))
        )

        # Находим элемент содержащий данные о логине пользователя
        email_field = user_logged_driver.find_element(*loc.ACCOUNT_FIELD_EMAIL)

        # Проверяем, что URL текущей страницы совпадает с ACCOUNT_PAGE и данные в поле "Логин" залогированного пользователя
        assert email_field.get_attribute("value") == RegisteredUser.email
        assert user_logged_driver.current_url == ACCOUNT_PAGE
