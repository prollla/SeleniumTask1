from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def moveToCartPage(self, driver):
        driver.find_element(By.LINK_TEXT, 'Checkout »').click()

    def isCartEmpty(self, driver):
        if len(driver.find_elements(By.XPATH, "//div[@id=\"order_confirmation-wrapper\"]")) > 0:
            return False
        else:
            return True

    def removeProduct(self, driver):
        loc = driver.find_element(By.NAME, "remove_cart_item")
        loc.click()
        WebDriverWait(driver, 10).until((EC.staleness_of(loc)))