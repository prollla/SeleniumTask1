from task19.pages.mainPage import MainPage
from task19.pages.productPage import ProductPage
from task19.pages.cartPage import CartPage


class Logic:

    def __init__(self, driver):
        self.mainPage = MainPage(driver)
        self.productPage = ProductPage(driver)
        self.cartPage = CartPage(driver)

    def addProductToCart(self, count):
        self.mainPage.moveToMainPage()
        for i in range(1, count+1):
            self.mainPage.moveToProductToCart()
            if self.productPage.isFindedElementSize():
                self.productPage.selectSizeDucks()
            self.productPage.addProduct()
            self.productPage.waitAddedToTheCart(i)

    def removeProduct(self):
        self.cartPage.moveToCartPage()
        while not self.cartPage.isCartEmpty():
            self.cartPage.removeProduct()
