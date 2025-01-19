from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


# Переход в Конструктор из личного кабинета по клику на «Конструктор»
def test_redirect_from_personal_account_to_constructor(credentials, driver):
    email = credentials["email"]
    password = credentials["password"]

    driver.find_element(*Locators.button_personal_account).click()
    driver.find_element(*Locators.field_email).send_keys(email)
    driver.find_element(*Locators.field_password).send_keys(password)
    driver.find_element(*Locators.button_login).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.button_personal_account))
    driver.find_element(*Locators.button_personal_account).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.href_profile))
    driver.find_element(*Locators.button_constructor).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.button_make_order))

    assert driver.find_element(*Locators.button_make_order).is_displayed()

# Переход в Конструктор из личного кабинета по клику на логотип Stellar Burgers
def test_redirect_from_personal_account_to_constructor_via_logo(credentials, driver):
    email = credentials["email"]
    password = credentials["password"]

    driver.find_element(*Locators.button_login_to_account).click()
    driver.find_element(*Locators.field_email).send_keys(email)
    driver.find_element(*Locators.field_password).send_keys(password)
    driver.find_element(*Locators.button_login).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.button_personal_account))
    driver.find_element(*Locators.button_personal_account).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.href_profile))
    driver.find_element(*Locators.logo_in_header).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.button_make_order))

    assert driver.find_element(*Locators.button_make_order).is_displayed()




