# Здесь собраны все используемые в автотестах сервиса Stellar Burgers локаторы
from selenium.webdriver.common.by import By


class Locators:

    # Поле "Имя" на форме регистрации
    FIELD_NAME = (
        By.XPATH,
        ".//label[text()='Имя']/following-sibling::input[@name='name']",
    )

    # Поле "Email" на форме регистрации/логина
    FIELD_EMAIL = (
        By.XPATH,
        ".//label[text()='Email']/following-sibling::input[@name='name']",
    )

    # Поле "Пароль" на форме регистрации/логина
    FIELD_PASSWORD = (By.XPATH, ".//input[@name='Пароль']")

    # Кнопка "Зарегистрироваться" на форме регистрации
    REGISTRATION_BTN = (By.XPATH, ".//button[text()='Зарегистрироваться']")

    # Кнопка "Войти" на форме логина
    LOGIN_BTN = (
        By.XPATH,
        ".//form[@class='Auth_form__3qKeq mb-20']//button[text()='Войти']",
    )

    # Кнопка "Оформить заказ" на главной странице авторизованного пользователя
    PLACE_ORDER_BTN = (
        By.XPATH,
        ".//button[text()='Оформить заказ']",
    )
    # Сообщение о некорректном пароле на странице регистрации
    PASSWORD_ERROR_MESSAGE = (By.XPATH, ".//p[text()='Некорректный пароль']")

    # Кнопка «Войти в аккаунт» на главной странице
    GO_TO_ACCOUNT_MAIN_PAGE_BTN = (
        By.XPATH,
        ".//button[text()='Войти в аккаунт']",
    )

    # Кнопка "Войти" на странице регистрации
    LOGIN_BTN_REGISTRATION = (
        By.XPATH,
        ".//p[text()='Уже зарегистрированы?']/a[@href and text()='Войти']",
    )

    # Кнопка "Войти" на странице восстановления пароля
    LOGIN_BTN_RESET_PASSWORD = (
        By.XPATH,
        ".//p[text()='Вспомнили пароль?']/a[@href and text()='Войти']",
    )

    #  Название выбранного раздела в шапке
    ACTIVE_SECTION_HEADER_TITLE = (
        By.XPATH,
        ".//a[@aria-current='page' and contains(@class, 'AppHeader_header') and contains(@class, 'link_active')]//p",
    )

    # Раздел "Личный Кабинет"
    ACCOUNT_HEADER_SECTION = (
        By.XPATH,
        ".//p[text()='Личный Кабинет']/parent::a[contains(@class, 'AppHeader_header')]",
    )

    # Раздел "Конструктор"
    CONSTRACTOR_HEADER_SECTION = (
        By.XPATH,
        ".//p[text()='Конструктор']/parent::a[contains(@class, 'AppHeader_header')]",
    )

    # Поле "Логин" на на странице "Личный Кабинет"
    ACCOUNT_FIELD_EMAIL = (
        By.XPATH,
        ".//label[text()='Логин']/following-sibling::input[@disabled]",
    )

    # Логотип Stellar Burgers на других страницах, кроме главной
    NOT_MAIN_PAGE_LOGO = (
        By.XPATH,
        ".//div[@class='AppHeader_header__logo__2D0X2']/a[@href]",
    )

    # Логотип Stellar Burgers на главной странице
    MAIN_PAGE_LOGO = (
        By.XPATH,
        ".//div[@class='AppHeader_header__logo__2D0X2']/a[@href and @aria-current='page']",
    )

    # Кпопка "Выход" на странице личного кабинета
    LOGOUT_BTN = (By.XPATH, ".//button[text()='Выход']")

    # Название формы для входа "Вход" на странице логина
    LOGIN_FORM_TITLE = (By.XPATH, ".//div/h2[text()='Вход']")

    # Название формы для регистрации "Регистрация" на странице регистрации
    REGISTRATION_FORM_TITLE = (By.XPATH, ".//div/h2[text()='Регистрация']")

    # Кнопка "Восстановить пароль" на странице входа
    RESET_PASSWORD_BTN = (By.XPATH, ".//a[@href and text()='Восстановить пароль']")

    # Выбранный подраздел в разделе "Конструктор"
    CONSTRUCTOR_ACTIVE_SUBSECTION = (
        By.XPATH,
        "//section[h1[text()='Соберите бургер']]//div[contains(@class,'tab_tab_type_current')]",
    )

    # Подраздел "Булки" в разделе "Конструктор"
    CONSTRUCTOR_SUBSECTION_BUNS = (
        By.XPATH,
        ".//section[h1[text()='Соберите бургер']]//div[span[text()='Булки']]",
    )

    # Подраздел "Соусы" в разделе "Конструктор"
    CONSTRUCTOR_SUBSECTION_SAUCES = (
        By.XPATH,
        ".//section[h1[text()='Соберите бургер']]//div[span[text()='Соусы']]",
    )

    # Подраздел "Начинки" в разделе "Конструктор"
    CONSTRUCTOR_SUBSECTION_FILLINGS = (
        By.XPATH,
        "//section[h1[text()='Соберите бургер']]//div[span[text()='Начинки']]",
    )
