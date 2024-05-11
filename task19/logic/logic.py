from task19.pages.mainPage import MainPage
from task19.pages.productPage import ProductPage
from task19.pages.cartPage import CartPage


class Logic:

    def __init__(self, driver):
        self.mainPage = MainPage(driver)
        self.productPage = ProductPage(driver)
        self.cartPage = CartPage(driver)

    def addProductToCart(self, driver):
        self.mainPage.moveToMainPage()
        for i in range(1, 4):
            self.mainPage.moveToProductToCart(driver)
            if self.productPage.isFindedElementSize(driver):
                self.productPage.selectSizeDucks(driver)
            self.productPage.addProduct(driver)
            self.productPage.waitAddedToTheCart(driver, i)

    def removeProduct(self, driver):
        self.cartPage.moveToCartPage(driver)
        while not self.cartPage.isCartEmpty(driver):
            self.cartPage.removeProduct(driver)
