from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


# Вход по кнопке «Войти в аккаунт» на главной странице
def test_login_main_page(credentials, driver):
    email = credentials["email"]
    password = credentials["password"]

    driver.find_element(*Locators.button_login_to_account).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.button_login))
    driver.find_element(*Locators.field_email).send_keys(email)
    driver.find_element(*Locators.field_password).send_keys(password)
    driver.find_element(*Locators.button_login).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.button_make_order))

    assert driver.find_element(*Locators.button_make_order).is_displayed()


# Вход через «Личный кабинет»
def test_login_my_account(credentials, driver):
    email = credentials["email"]
    password = credentials["password"]

    driver.find_element(*Locators.button_personal_account).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.button_login))
    driver.find_element(*Locators.field_email).send_keys(email)
    driver.find_element(*Locators.field_password).send_keys(password)
    driver.find_element(*Locators.button_login).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.button_make_order))

    assert driver.find_element(*Locators.button_make_order).is_displayed()


# Вход через кнопку «Войти» в форме регистрации
def test_login_registration_form(credentials, driver):
    email = credentials["email"]
    password = credentials["password"]

    driver.find_element(*Locators.button_login_to_account).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.href_register))
    driver.find_element(*Locators.href_register).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.button_register))
    driver.find_element(*Locators.href_login).click()
    driver.find_element(*Locators.field_email).send_keys(email)
    driver.find_element(*Locators.field_password).send_keys(password)
    driver.find_element(*Locators.button_login).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.button_make_order))

    assert driver.find_element(*Locators.button_make_order).is_displayed()


# Вход через кнопку «Войти» в форме восстановления пароля
def test_login_password_recovery(credentials, driver):
    email = credentials["email"]
    password = credentials["password"]

    driver.find_element(*Locators.button_personal_account).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.href_recover_password))
    driver.find_element(*Locators.href_recover_password).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.href_login))
    driver.find_element(*Locators.href_login).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.button_login))
    driver.find_element(*Locators.field_email).send_keys(email)
    driver.find_element(*Locators.field_password).send_keys(password)
    driver.find_element(*Locators.button_login).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.button_make_order))

    assert driver.find_element(*Locators.button_make_order).is_displayed()