import random
import string
import time
import os
from selenium.webdriver.support import expected_conditions as EC

import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


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
        color_values = color[5:-1].split(', ')
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
        color_values = color[5:-1].split(', ')
        if color_values[1] == color_values[2] == "0":
            pass
        else:
            pytest.fail("Цвет не красный")


def test_example8(driver):
    email = generate_email()
    password = "123"
    driver.maximize_window()
    driver.get("http://localhost/litecart/en/")
    driver.find_element(By.LINK_TEXT, "New customers click here").click()
    driver.find_element(By.NAME, "firstname").send_keys("Anton")
    driver.find_element(By.NAME, "lastname").send_keys("Anton")
    driver.find_element(By.NAME, "address1").send_keys("Anton")
    driver.find_element(By.NAME, "postcode").send_keys("12345")
    driver.find_element(By.NAME, "city").send_keys("Anton")
    driver.find_element(By.NAME, "phone").send_keys("+123456789")
    """driver.find_element(By.CLASS_NAME, "selection").click()
    driver.find_element(By.XPATH, "//li[contains(text(), 'United States')]").click() """
    select = driver.find_element(By.CSS_SELECTOR, "select")
    driver.execute_script("arguments[0].selectedIndex=224; arguments[0].dispatchEvent(new Event('change'))", select)
    driver.find_element(By.NAME, "email").send_keys(email)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.NAME, "confirmed_password").send_keys(password)
    driver.find_element(By.NAME, "create_account").click()
    driver.find_element(By.LINK_TEXT, "Logout").click()
    driver.find_element(By.NAME, "email").send_keys(email)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.NAME, "login").click()
    driver.find_element(By.LINK_TEXT, "Logout").click()


def generate_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(5, 10)))
    email = username + "@mail.ru"
    return email


def test_example9(driver):
    driver.maximize_window()
    driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog")
    driver.find_element(By.NAME, 'username').send_keys("admin")
    driver.find_element(By.NAME, 'password').send_keys("admin")
    driver.find_element(By.NAME, 'remember_me').click()
    driver.find_element(By.NAME, 'login').click()
    driver.find_element(By.LINK_TEXT, 'Add New Product').click()
    name = generate_name()
    driver.find_element(By.NAME, 'name[en]').send_keys(name)
    driver.find_element(By.XPATH, '//input[@type="radio" and @value="1"]').click()
    driver.find_element(By.NAME, 'code').send_keys("255")
    driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox'][name='product_groups[]']")[2].click()
    driver.find_element(By.NAME, 'quantity').send_keys("1500")
    current_directory = os.path.dirname(os.path.abspath(__file__))
    driver.find_element(By.NAME, 'new_images[]').send_keys(os.path.join(current_directory, 'product.jpg'))
    driver.find_element(By.NAME, 'date_valid_from').send_keys('24-04-2024')
    driver.find_element(By.NAME, 'date_valid_to').send_keys('01-05-2024')
    '''driver.find_element(By.NAME, 'date_valid_from').send_keys('2024-04-24') #Firefox
    driver.find_element(By.NAME, 'date_valid_to').send_keys('2024-05-01') #Firefox'''
    driver.find_element(By.LINK_TEXT, 'Information').click()
    select_element = driver.find_element(By.NAME, 'manufacturer_id')
    select = Select(select_element)
    select.select_by_value('1')
    driver.find_element(By.NAME, 'keywords').send_keys('product')
    driver.find_element(By.NAME, 'short_description[en]').send_keys('product')
    driver.find_element(By.CLASS_NAME, 'trumbowyg-editor').send_keys('product')
    driver.find_element(By.NAME, 'head_title[en]').send_keys('product')
    driver.find_element(By.NAME, 'meta_description[en]').send_keys('product')
    driver.find_element(By.LINK_TEXT, 'Data').click()
    driver.find_element(By.NAME, 'sku').send_keys('123')
    driver.find_element(By.NAME, 'gtin').send_keys('123')
    driver.find_element(By.NAME, 'taric').send_keys('123')
    driver.find_element(By.NAME, 'weight').send_keys('123')
    driver.find_element(By.NAME, 'dim_x').send_keys('2')
    driver.find_element(By.NAME, 'dim_y').send_keys('2')
    driver.find_element(By.NAME, 'dim_z').send_keys('2')
    driver.find_element(By.NAME, 'save').click()
    driver.find_element(By.LINK_TEXT, name).click()


def generate_name():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(5, 10)))
    return username


def test_example10(driver):
    driver.maximize_window()
    driver.get('http://localhost/litecart')
    for i in range(1, 4):
        box = driver.find_element(By.ID, 'box-most-popular')
        box.find_element(By.CLASS_NAME, 'name').click()
        try:
            select = driver.find_element(By.CSS_SELECTOR, "select")
            driver.execute_script("arguments[0].selectedIndex=1; arguments[0].dispatchEvent(new Event('change'))",
                                  select)
        except:
            pass
        driver.find_element(By.NAME, 'add_cart_product').click()
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'quantity'), str(i)))
        driver.back()
    driver.find_element(By.LINK_TEXT, 'Checkout »').click()
    time.sleep(5)
    elements = driver.find_elements(By.XPATH, "//td[@class='item']")
    for i in range(len(elements)):
        try:
            remove_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.NAME, 'remove_cart_item')))  #Находим элемент
            remove_button.click()  #Кликаем
            WebDriverWait(driver, 5).until(EC.staleness_of(remove_button))  #Ждём пока исчезнет
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.NAME, 'remove_cart_item')))
        except:
            driver.find_element(By.LINK_TEXT, "<< Back").click()


def test_example11(driver):
    driver.maximize_window()
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    driver.find_element(By.NAME, 'username').send_keys("admin")
    driver.find_element(By.NAME, 'password').send_keys("admin")
    driver.find_element(By.NAME, 'remember_me').click()
    driver.find_element(By.NAME, 'login').click()
    driver.find_element(By.LINK_TEXT, 'Add New Country').click()
    links = driver.find_elements(By.CSS_SELECTOR, "i.fa.fa-external-link")
    for link in links:
        link.click()
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        driver.switch_to.window(driver.window_handles[-1])
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        time.sleep(2)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
    time.sleep(5)


def test_example12(driver):
    driver.maximize_window()
    driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")
    driver.find_element(By.NAME, 'username').send_keys("admin")
    driver.find_element(By.NAME, 'password').send_keys("admin")
    driver.find_element(By.NAME, 'remember_me').click()
    driver.find_element(By.NAME, 'login').click()
    colspan_element = driver.find_element(By.XPATH, '//td[@colspan]')
    colspan_value = int(colspan_element.get_attribute("colspan"))
    browser_logs = []
    for i in range(colspan_value, colspan_value * 2):
        product_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//*[@id='content']/form/table/tbody/tr[{i}]/td[3]/a")))
        product_link.click()
        logs = driver.get_log('browser')
        browser_logs.extend(logs)
        driver.back()
    for log in browser_logs:
        print(log)
