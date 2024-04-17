import time

import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


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
    li_elements = driver.find_elements(By.CSS_SELECTOR, "li.product")
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


def test_example5(driver):
    driver.maximize_window()
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    driver.find_element(By.NAME, 'username').send_keys("admin")
    driver.find_element(By.NAME, 'password').send_keys("admin")
    driver.find_element(By.NAME, 'remember_me').click()
    driver.find_element(By.NAME, 'login').click()
    elements = driver.find_elements(By.CSS_SELECTOR, "table.dataTable")
    names = []
    names_geozones = []
    for element in elements:
        lines = element.find_elements(By.CSS_SELECTOR, "td:nth-child(5), td:nth-child(6)")

        for i in range(0, len(lines), 2):
            name_element = lines[i]
            count_element = lines[i + 1]
            if name_element.text.strip() and count_element.text.strip():
                names.append(name_element.text)
                if count_element.text != "0":
                    driver.find_element(By.LINK_TEXT, name_element.text).click()
                    elements = driver.find_elements(By.CSS_SELECTOR, "table.dataTable")
                    for element in elements:
                        names_geozones.append(element.text)
                    driver.back()
                    element = driver.find_element(By.CSS_SELECTOR, "table.dataTable")
                    lines = element.find_elements(By.CSS_SELECTOR, "td:nth-child(5), td:nth-child(6)")
    is_sorted = names == sorted(names) and names_geozones == sorted(names_geozones)
    if is_sorted:
        print("Sorted")
    else:
        pytest.fail("No sorted")


def test_example6(driver):
    driver.maximize_window()
    driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
    driver.find_element(By.NAME, 'username').send_keys("admin")
    driver.find_element(By.NAME, 'password').send_keys("admin")
    driver.find_element(By.NAME, 'remember_me').click()
    driver.find_element(By.NAME, 'login').click()
    elements = driver.find_elements(By.CSS_SELECTOR, "table.dataTable td:nth-child(3)")
    links_text = [element.text for element in elements]
    names = []
    for text in links_text:
        names.clear()
        link = driver.find_element(By.LINK_TEXT, text).click()
        select_elements = driver.find_elements(By.CSS_SELECTOR, 'select[name^="zones["][name$="][zone_code]"]')
        for select_element in select_elements:
            select = Select(select_element)
            selected_option = select.first_selected_option
            names.append(selected_option.text)
        driver.back()
        is_sorted = names == sorted(names)
        if is_sorted:
            print("Sotred")
        else:
            pytest.fail("Not sorted")
        elements = driver.find_elements(By.CSS_SELECTOR, "table.dataTable a")
        links_text = [element.text for element in elements]







