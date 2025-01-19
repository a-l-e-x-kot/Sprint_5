from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


# Выход из аккаунта по кнопке «Выйти» в личном кабинете
def test_logout(credentials, driver):
    email = credentials["email"]
    password = credentials["password"]

    driver.find_element(*Locators.button_personal_account).click()
    driver.find_element(*Locators.field_email).send_keys(email)
    driver.find_element(*Locators.field_password).send_keys(password)
    driver.find_element(*Locators.button_login).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.button_personal_account))
    driver.find_element(*Locators.button_personal_account).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.button_exit))

    driver.find_element(*Locators.button_exit).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.button_login))

    assert driver.find_element(*Locators.button_login).is_displayed()