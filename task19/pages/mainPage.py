from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.mainUrl = ("http://localhost/litecart/en/")
        self.wait = WebDriverWait(driver, 10)

    def moveToMainPage(self):
        return self.driver.get(self.mainUrl)

    def moveToProductToCart(self):
        box = self.driver.find_element(By.ID, 'box-most-popular')
        box.find_element(By.CLASS_NAME, 'name').click()