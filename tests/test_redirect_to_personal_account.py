from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


# Переход в личный кабинет
def test_redirect_to_personal_account(credentials, driver):
    email = credentials["email"]
    password = credentials["password"]

    driver.find_element(*Locators.button_personal_account).click()
    driver.find_element(*Locators.field_email).send_keys(email)
    driver.find_element(*Locators.field_password).send_keys(password)
    driver.find_element(*Locators.button_login).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.button_personal_account))
    driver.find_element(*Locators.button_personal_account).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.href_profile))

    assert driver.find_element(*Locators.href_order_history).is_displayed()