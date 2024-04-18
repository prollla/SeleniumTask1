import time

import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.fixture()
def driver(request):
    driver = webdriver.Chrome()
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
                    elements = driver.find_elements(By.CSS_SELECTOR, "table.dataTable td:nth-child(3)")
                    for element in elements:
                        if element.text.strip():
                            names_geozones.append(element.text)
                    driver.back()
                    print(names_geozones)
                    is_sorted = names_geozones == sorted(names_geozones)
                    if is_sorted:
                        print("Sorted name_geozones")
                    else:
                        pytest.fail("Not sorted")
                    names_geozones.clear()
                    element = driver.find_element(By.CSS_SELECTOR, "table.dataTable")
                    lines = element.find_elements(By.CSS_SELECTOR, "td:nth-child(5), td:nth-child(6)")
    is_sorted = names == sorted(names)
    if is_sorted:
        print("Sorted name")
    else:
        pytest.fail("Not sorted")


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


"""def test_example7(driver):
    driver.maximize_window()
    main_product_data = []
    another_product_data = []
    driver.get("http://localhost/litecart")
    box = driver.find_element(By.ID, "box-campaigns")
    product = box.find_element(By.CLASS_NAME, "name")
    main_product_data.append(product.text)
    price = box.find_element(By.CLASS_NAME, "regular-price")
    text_decoration = price.value_of_css_property('text-decoration')
    strike(text_decoration, price)
    main_product_data.append(price.text)
    campaign_price = box.find_element(By.CLASS_NAME, "campaign-price")
    text_decoration = campaign_price.value_of_css_property('text-decoration')
    solid(text_decoration, campaign_price)
    size(price, campaign_price)
    main_product_data.append(campaign_price.text)
    product.click()

    box = driver.find_element(By.ID, "box-product")
    product = box.find_element(By.CLASS_NAME, "title")
    another_product_data.append(product.text)
    price = driver.find_element(By.CLASS_NAME, "regular-price")
    text_decoration = price.value_of_css_property('text-decoration')
    strike(text_decoration, price)
    another_product_data.append(price.text)
    campaign_price = driver.find_element(By.CLASS_NAME, "campaign-price")
    text_decoration = campaign_price.value_of_css_property('text-decoration')
    solid(text_decoration, campaign_price)
    size(price, campaign_price)
    another_product_data.append(campaign_price.text)
    if another_product_data == main_product_data:
        pass
    else:
        pytest.fail("Not equals")


def size(price, campaign_price):
    regular_font_size = float(price.value_of_css_property('font-size')[:-2])
    campaign_font_size = float(campaign_price.value_of_css_property('font-size')[:-2])
    if campaign_font_size > regular_font_size:
        pass
    else:
        pytest.fail('Размер шрифта у цены по акции не больше регулярной цены')


def strike(text_decoration, price):
    color = price.value_of_css_property('color')
    is_strikethrough = 'line-through' in text_decoration
    if is_strikethrough:
        color_values = color[5:-1].split(', ')
        r, g, b, l = map(int, color_values)
        is_same_color = r == g == b
        if is_same_color:
            pass
        else:
            pytest.fail("Цвет не серый")
    else:
        pytest.fail("Текст не зачёркнут")


def solid(text_decoration, campaign_price):
    color = campaign_price.value_of_css_property('color')
    is_solid = 'solid' in text_decoration
    if is_solid:
        color_values = color[5:-1].split(', ')
        r, g, b, l = map(int, color_values)
        if g == b == 0:
            pass
        else:
            pytest.fail("Цвет не красный") """


def test_example7(driver):
    driver.maximize_window()
    product_data = [[], []]
    driver.get("http://localhost/litecart")
    for i in range(2):
        get_product_data(driver, product_data, i)
    if product_data[0] == product_data[1]:
        pass
    else:
        pytest.fail("Not equals")


def get_product_data(driver, product_data, i):
    if i == 0:
        box = driver.find_element(By.ID, "box-campaigns")
        product = box.find_element(By.CLASS_NAME, "name")
    else:
        box = driver.find_element(By.ID, "box-product")
        product = box.find_element(By.CLASS_NAME, "title")
    product_data[i].append(product.text)
    price = driver.find_element(By.CLASS_NAME, "regular-price")
    text_decoration = price.value_of_css_property('text-decoration')
    strike(text_decoration, price)
    product_data[i].append(price.text)
    campaign_price = driver.find_element(By.CLASS_NAME, "campaign-price")
    text_decoration = campaign_price.value_of_css_property('text-decoration')
    solid(text_decoration, campaign_price)
    size(price, campaign_price)
    product_data[i].append(campaign_price.text)
    if i == 0:
        product.click()
    else:
        pass
    return product_data


def size(price, campaign_price):
    regular_font_size = float(price.value_of_css_property('font-size')[:-2])
    campaign_font_size = float(campaign_price.value_of_css_property('font-size')[:-2])
    if campaign_font_size > regular_font_size:
        pass
    else:
        pytest.fail('Размер шрифта у цены по акции не больше регулярной цены')


def strike(text_decoration, price):
    color = price.value_of_css_property('color')
    is_strikethrough = 'line-through' in text_decoration
    if is_strikethrough:
        color_values = color[4:-1].split(', ')
        is_same_color = color_values[0] == color_values[1] == color_values[2]
        if is_same_color:
            pass
        else:
            pytest.fail("Цвет не серый")
    else:
        pytest.fail("Текст не зачёркнут")


def solid(text_decoration, campaign_price):
    color = campaign_price.value_of_css_property('color')
    is_solid = 'solid' in text_decoration
    if is_solid:
        color_values = color[4:-1].split(', ')
        if color_values[1] == color_values[2] == "0":
            pass
        else:
            pytest.fail("Цвет не красный")
