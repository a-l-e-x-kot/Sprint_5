from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


# Раздел «Конструктор». Переход в раздел "Булки"
def test_navigate_to_buns(driver):
    driver.find_element(*Locators.span_toppings).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.subsection_toppings))
    driver.find_element(*Locators.span_buns).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.subsection_buns))
    assert "Булки" in driver.find_element(*Locators.subsection_buns).text
    assert "Начинки" in driver.find_element(*Locators.subsection_toppings).text


# Раздел «Конструктор». Переход в раздел "Соусы"
def test_navigate_to_sauces(driver):
    driver.find_element(*Locators.span_sauces).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.subsection_sauces))
    assert "Соусы" in driver.find_element(*Locators.subsection_sauces).text


# Раздел «Конструктор». Переход в раздел "Начинки"
def test_navigate_to_toppings(driver):
    driver.find_element(*Locators.span_toppings).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.subsection_toppings))
    assert "Начинки" in driver.find_element(*Locators.subsection_toppings).text
