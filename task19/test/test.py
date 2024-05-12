import pytest
from task19.logic.logic import Logic
from selenium import webdriver


@pytest.fixture
def driver(request):
    driver = webdriver.Chrome()
    request.addfinalizer(driver.quit)
    return driver


def test_example(driver):
    app = Logic(driver)
    app.addProductToCart()
    app.removeProduct()
