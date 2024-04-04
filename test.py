import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def driver(request):
    driver = webdriver.Edge()
    request.addfinalizer(driver.quit)
    return driver


def test_example(driver):
    driver.maximize_window()
    driver.get("https://www.google.com")
    time.sleep(2)


def test_example2(driver):
    driver.maximize_window()
    driver.get("http://localhost/litecart/admin/")
    driver.find_element(By.NAME, 'username').send_keys("admin")
    driver.find_element(By.NAME, 'password').send_keys("admin")
    driver.find_element(By.NAME, 'remember_me').click()
    time.sleep(1)
    driver.find_element(By.NAME, 'login').click()
    time.sleep(2)