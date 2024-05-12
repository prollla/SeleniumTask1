from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def isFindedElementSize(self):
        elements = self.driver.find_elements(By.XPATH, "//select[@name=\"options[Size]\"]")
        if len(elements) > 0:
            return True
        else:
            return False

    def selectSizeDucks(self):
        select = self.driver.find_element(By.CSS_SELECTOR, "select")
        self.driver.execute_script("arguments[0].selectedIndex=1; arguments[0].dispatchEvent(new Event('change'))",
                              select)

    def addProduct(self):
        self.driver.find_element(By.NAME, 'add_cart_product').click()

    def waitAddedToTheCart(self, i):
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'quantity'), str(i)))
        self.driver.back()