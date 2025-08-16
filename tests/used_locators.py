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
    # Сообщение о некорректном пароле на странице регистрации
    password_error_message = (By.XPATH, ".//p[text()='Некорректный пароль']")

    # Кнопка «Войти в аккаунт» на главной странице
    go_to_account_main_btn = (
        By.XPATH,
        ".//*[@id='root']/div/main/section[2]/div/button[text()='Войти в аккаунт']",
    )

    # Кнопка «Личный кабинет» на главной странице
    account_btn_main = (
        By.XPATH,
        ".//a[p[text()='Личный Кабинет']]",
    )

    # Кнопка "Войти" на странице регистрации
    login_btn_registration = (
        By.XPATH,
        ".//p[text()='Уже зарегистрированы?']/a[@href and text()='Войти']",
    )

    # Кнопка "Войти" на странице восстановления пароля
    login_btn_rest_password = (
        By.XPATH,
        ".//p[text()='Вспомнили пароль?']/a[@href and text()='Войти']",
    )

    # Название активного раздела "Личный Кабинет" на странице "Личный Кабинет"
    account_page_title = (
        By.XPATH,
        ".//p[text()='Личный Кабинет']/parent::a[@aria-current='page' and contains(@class, 'link_active')]",
    )

    # Поле "Логин" на на странице "Личный Кабинет"
    account_page_field_email = (
        By.XPATH,
        ".//ul/li//label[text()='Логин']/following-sibling::input[@disabled]",
    )

    # Раздел "Конструктор" на странице личного кабинета
    account_page_constructor_section = (
        By.XPATH,
        ".//ul/li//p[text()='Конструктор']/parent::a",
    )

    # Название активного раздела "Конструктор" на главной странице
    constructor_section_main_page = (
        By.XPATH,
        ".//p[text()='Конструктор']/parent::a[@aria-current='page' and contains(@class, 'link_active')]",
    )

    # Логотип Stellar Burgers на других страницах
    another_page_logo = (
        By.XPATH,
        ".//div[@class='AppHeader_header__logo__2D0X2']/a[@href]",
    )

    # Логотип Stellar Burgers на главной странице
    main_page_logo = (
        By.XPATH,
        ".//div[@class='AppHeader_header__logo__2D0X2']/a[@href and @aria-current='page']",
    )

    # Кпопка "Выход" на странице личного кабинета
    logout_btn_account_page = (By.XPATH, ".//ul/li/button[text()='Выход']")

    # Название формы для входа "Вход" на странице логина
    login_form_header = (By.XPATH, ".//div/h2[text()='Вход']")

    # Название формы для регистрации "Регистрация" на странице регистрации
    registration_form_header = (By.XPATH, ".//div/h2[text()='Регистрация']")

    # Кнопка "Восстановить пароль" на странице входа
    reset_password_btn = (By.XPATH, ".//a[@href and text()='Восстановить пароль']")

    # Выбранный подраздел в разделе "Конструктор"
    constructor_section_active = (
        By.XPATH,
        "//section[h1[text()='Соберите бургер']]//div[contains(@class,'tab_tab_type_current')]",
    )

    # Подраздел "Булки" в разделе "Конструктор"
    constructor_section_buns = (By.XPATH, ".//section[h1[text()='Соберите бургер']]//div[span[text()='Булки']]")

    # Подраздел "Соусы" в разделе "Конструктор"
    constructor_section_sauces = (By.XPATH, ".//section[h1[text()='Соберите бургер']]//div[span[text()='Соусы']]")

    # Подраздел "Начинки" в разделе "Конструктор"
    constructor_section_fillings = (By.XPATH, "//section[h1[text()='Соберите бургер']]//div[span[text()='Начинки']]")
