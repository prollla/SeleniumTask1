import time

import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
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


def test_example3(driver):
    driver.maximize_window()
    driver.get("http://localhost/litecart/admin/")
    driver.find_element(By.NAME, 'username').send_keys("admin")
    driver.find_element(By.NAME, 'password').send_keys("admin")
    driver.find_element(By.NAME, 'remember_me').click()
    time.sleep(1)
    driver.find_element(By.NAME, 'login').click()
    time.sleep(2)
    li_elements = driver.find_elements(By.CSS_SELECTOR, "ul#box-apps-menu li#app-")
    for index in range(len(li_elements)):
        li_elements = driver.find_elements(By.CSS_SELECTOR, "ul#box-apps-menu li#app-")
        li_elements[index].click()
        time.sleep(1)
        try:
            li_secret = driver.find_elements(By.CSS_SELECTOR, "#box-apps-menu li.selected li")
            for i in range(len(li_secret)):
                li_secret = driver.find_elements(By.CSS_SELECTOR, "#box-apps-menu li.selected li")
                li_secret[i].click()
                time.sleep(1)
                try:
                    h1_element = driver.find_element(By.TAG_NAME, "h1")
                    print(h1_element.text)
                except NoSuchElementException:
                    pytest.fail("Element not found")
        except NoSuchElementException:
            try:
                h1_element = driver.find_element(By.TAG_NAME, "h1")
                print(h1_element.text)
            except NoSuchElementException:
                pytest.fail("Element not found")


def test_example4(driver):
    driver.maximize_window()
    driver.get("http://localhost/litecart/en/")
    time.sleep(1)
    li_elements = driver.find_elements(By.CSS_SELECTOR, "ul.listing-wrapper li.product")
    for element in li_elements:
        stickers = element.find_elements(By.CSS_SELECTOR, ".sticker")

        if len(stickers) == 1:
            if stickers[0].get_attribute("class") == "sticker sale":
                print("Sale")
            elif stickers[0].get_attribute("class") == "sticker new":
                print("New")
            else:
                print("Another sticker")
        else:
            pytest.fail("Количество стикеров не равно одному")
