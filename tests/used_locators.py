# Здесь собраны все используемые в проекте локаторы
from selenium.webdriver.common.by import By


class Locators:

    # Поле "Имя" на форме регистрации
    field_name = (
        By.XPATH,
        ".//label[text()='Имя']/following-sibling::input[@name='name']",
    )

    # Поле "Email" на форме регистрации/логина
    field_email = (
        By.XPATH,
        ".//label[text()='Email']/following-sibling::input[@name='name']",
    )

    # Поле "Пароль" на форме регистрации/логина
    field_password = (By.XPATH, ".//input[@name='Пароль']")
    
    # Кнопка "Зарегистрироваться" на форме регистрации
    registration_btn = (By.XPATH, ".//button[text()='Зарегистрироваться']")  
    
    # Кнопка "Войти" на форме логина
    login_btn = (
        By.XPATH,
        ".//form[@class='Auth_form__3qKeq mb-20']//button[text()='Войти']",
    )

    # Кнопка "Оформить заказ" на главной странице авторизованного пользователя
    place_order_btn = (
        By.XPATH,
        ".//*[@id='root']/div/main/section[2]/div/button[text()='Оформить заказ']",
    )
