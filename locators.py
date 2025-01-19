from selenium.webdriver.common.by import By


class Locators:
    button_personal_account = (By.XPATH, '//p[text() = "Личный Кабинет"]')  # Кнопка "Личный кабинет"

    button_login_to_account = (By.XPATH, './/button[text() = "Войти в аккаунт"]')  # Кнопка "Войти в аккаунт" на главной странице

    button_register = (By.XPATH, '//button[text() = "Зарегистрироваться"]') # Кнопка "Зарегистрироваться"

    href_register = (By.XPATH, '//a[text() = "Зарегистрироваться"]')  # Гиперссылка "Зарегистрироваться"

    field_name = (By.XPATH, ".//label[text()='Имя']//parent::*/input[@type='text' and @name='name']")  # Поле "Имя"

    field_email = (By.XPATH, ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']")  # Поле "Email"

    field_password = (By.XPATH, ".//input[@type='password' and @name='Пароль']")  # Поле "Пароль"

    button_login =  (By.XPATH, './/button[text()="Войти"]')  # Кнопка "Войти"

    href_login = (By.XPATH, '//a[text() = "Войти"]')  # Гиперссылка "Войти" в форме регистрации

    error_message_password = (By.XPATH, '//p[text() = "Некорректный пароль"]')  # Сообщение об ошибке "Некорректный пароль"

    button_make_order = (By.XPATH, '//button[text()="Оформить заказ"]')  # Кнопка "Оформить заказ"

    href_recover_password = (By.XPATH, '//a[text() = "Восстановить пароль"]') # Гиперссылка "Восстановить пароль"

    href_profile = (By.XPATH, '//a[@href = "/account/profile"]')  # Раздел "Профиль"

    href_order_history = (By.XPATH, '//a[@href = "/account/order-history"]')  # Раздел "История заказов"

    button_constructor = (By.XPATH, '//p[text() = "Конструктор"]')  # Кнопка "Конструктор"

    logo_in_header = (By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]')  # Лого в шапке сайта

    button_exit = (By.XPATH, '//button[text()="Выход"]')  # Кнопка "Выход" в личном кабинете

    span_buns = (By.XPATH, "//span[text()='Булки']")  # Раздел "Булки"

    span_sauces = (By.XPATH, "//span[text()='Соусы']")  # раздел "Соусы"

    span_toppings = (By.XPATH, '//span[text() = "Начинки"]')  # Раздел "Начинки"

    subsection_buns = (By.XPATH, ".//h2[text()='Булки']")  # Подраздела "Булки" в разделе «Конструктор»

    subsection_sauces = (By.XPATH, ".//h2[text()='Соусы']")  # Подраздела "Соусы" в разделе «Конструктор»

    subsection_toppings = (By.XPATH,".//h2[text()='Начинки']")  # Подраздела "Начинки" в разделе «Конструктор»