from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import main_url, account_url
from used_locators import Locators as loc


class TestRedirectToAccount:
    # Проверка перехода в личный кабинет  по клику на «Личный кабинет».
    def test_redirect_to_account_from_main(self, user_logged_driver, registered_user):

        # Откроем главную страницу в окне браузера как залогированный пользователь
        user_logged_driver.get(main_url)

        # Кликнем на «Личный кабинет» на главной странице
        user_logged_driver.find_element(*loc.account_btn_main).click()

        # Добавляем явное ожидание, что название раздела загрузилось
        WebDriverWait(user_logged_driver, 10).until(
            EC.visibility_of_element_located((loc.account_page_title))
        )

        # Добавляем явное ожидание, что форма с данными пользователя (поле "Логин") загрузилась
        WebDriverWait(user_logged_driver, 10).until(
            EC.visibility_of_element_located((loc.account_page_field_email))
        )
        # Находим элемент содержащий данные о логине пользователя
        email_field_account = user_logged_driver.find_element(*loc.account_page_field_email)

        # Проверка, что URL текущей страницы совпадает с account_url и данные в поле "Логин" залогированного пользователя
        assert email_field_account.get_attribute("value") == registered_user["email"]
        assert user_logged_driver.current_url == account_url
