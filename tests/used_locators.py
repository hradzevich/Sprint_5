# Здесь собраны все используемые в проекте локаторы
registration_form = ".//form[@class='Auth_form__3qKeq mb-20']"
registration_form_name = ".//label[text()='Имя']/following-sibling::input[@name='name']"  # Поле "Имя" на форме регистрации
registration_form_email = ".//label[text()='Email']/following-sibling::input[@name='name']"  # Поле "Email" на форме регистрации
registration_form_password = (
    ".//input[@name='Пароль']"  # Поле "Пароль" на форме регистрации
)
registration_btn = ".//button[text()='Зарегистрироваться']"  # Кнопка "Зарегистрироваться" на форме регистрации
login_form = ".//form[@class='Auth_form__3qKeq mb-20']"  # Форма для логина
login_form_email = ".//label[text()='Email']/following-sibling::input[@name='name']"  # Поле "Email" на форме логина
login_form_password = ".//input[@name='Пароль']"  # Поле "Пароль" на форме логина
login_btn = ".//button[text()='Войти']"  # Кнопка "Войти" на форме логина
place_order_btn = ".//button[text()='Оформить заказ']"  # Кнопка "Оформить заказ" на главной странице авторизованного пользователя
