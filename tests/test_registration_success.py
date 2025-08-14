from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import register_url
import used_locators


class TestRegistration:
    # Проверка регистрации нового пользователя с валидными логином(email в формате логин@домен) и паролем(длина болеее 6 символов)
    def test_registration_valid_credentials_success(
        self, chrome_driver, credentials_for_registration
    ):
        chrome_driver.get(register_url)
