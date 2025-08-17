# <span style= "color: yellow">**Stellar Burgers Autotests**</span> 

Это учебный проект Yandex.Practicum содержит автотесты на Python содержит автотесты для учебного приложения Stellar Burgers (космический фастфуд: можно собрать и заказать бургер из необычных ингредиентов).

## <span style= "color: cornflowerblue">Реализованные тесты:</span> 

### Регистрация

Успешная регистрация (валидные данные) 	***`test_registration_valid_credentials_success`***

Ошибка при некорректном пароле (< 6 символов).
***`test_registration_invalid_password_error`***

### Вход

Вход по кнопке «Войти в аккаунт» на главной ***`test_login_from_main_page_via_login_button`***

Вход через «Личный кабинет» ***`test_login_from_main_via_account_button`***

Вход через форму регистрации ***`test_login_from_registration`***

Вход через форму восстановления пароля ***`test_login_via_password_reset`***

### Переход в личный кабинет

Переход по клику на «Личный кабинет» ***`test_redirect_to_account_from_main`***

### Переход из личного кабинета в конструктор 

Из личного кабинета в конструктор (по разделу «Конструктор») ***`test_redirect_to_constructor_by_click`***

Из личного кабинета в конструктор (по клику на логотип) ***`test_redirect_to_constructor_by_logo_click`***

### Выход из аккаунта

Выход из аккаунта через кнопку «Выйти» ***`test_logout_from_account_by_logout_btn_click`***

### Раздел «Конструктор»

Переключение между разделами:<br/>
«Булки» ***`test_navigation_in_constructor_to_buns`***
«Соусы» ***`test_navigation_in_constructor_to_sauces`***
«Начинки» ***`test_navigation_in_constructor_to_fillings`***

## <span style= "color: cornflowerblue">Технологии</span>

+ Python 3.13.5

+ Pytest

+ Selenium

+ Faker (для генерации тестовых данных)


## <span style= "color: cornflowerblue">Запуск тестов</span>

1. Клонировать репозиторий:<br/>
     ```shell git clone https://github.com/hradzevich/Sprint_5.git  ```

2. Установить зависимости:<br/>
     ```shell pip install -r requirements.txt```

3. Запустить тесты:<br/>
     ```shell pytest -v```
