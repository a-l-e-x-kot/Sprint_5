from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random_generator import generate_name, generate_email, generate_password, generate_invalid_password
from locators import Locators

# Успешная регистрации
def test_registration_success(driver):
    user_name = generate_name()
    user_email = generate_email()
    user_password = generate_password()

    driver.find_element(*Locators.button_login_to_account).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.href_register))

    driver.find_element(*Locators.href_register).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.button_register))

    driver.find_element(*Locators.field_name).send_keys(user_name)
    driver.find_element(*Locators.field_email).send_keys(user_email)
    driver.find_element(*Locators.field_password).send_keys(user_password)
    driver.find_element(*Locators.button_register).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.button_login))

    assert driver.find_element(*Locators.button_login).is_displayed()


# Сообщение об ошибке для невалидного пароля
def test_registration_error_message_password(driver):
    user_name = generate_name()
    user_email = generate_email()
    user_invalid_password = generate_invalid_password()


    driver.find_element(*Locators.button_login_to_account).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.href_register))

    driver.find_element(*Locators.href_register).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.button_register))

    driver.find_element(*Locators.field_name).send_keys(user_name)
    driver.find_element(*Locators.field_email).send_keys(user_email)
    driver.find_element(*Locators.field_password).send_keys(user_invalid_password)
    driver.find_element(*Locators.button_register).click()

    WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.error_message_password))

    assert driver.find_element(*Locators.error_message_password).text == 'Некорректный пароль'