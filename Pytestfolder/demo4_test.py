import time
import re
import random
import string
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Chromeservice
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=Chromeservice(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def is_valid_email(email):
    email_pattern = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.search(email_pattern, email))


def generate_random_email():
    length = random.randint(4, 11)
    characters = string.ascii_lowercase + string.digits

    if random.random() < 0.2:
        characters += '.'
    elif random.random() < 0.3:
        characters += '_'
    domain = '@tst.com'

    local_part = ''.join(random.choice(characters) for _ in range(5))
    email = local_part + domain
    return email


def generate_random_name():
    name = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
    return name


def generate_random_number():
    # The first two digits are 98
    start = "98"
    # Generate the remaining 8 digits randomly
    remaining_digits = ''.join([str(random.randint(0, 9)) for _ in range(8)])
    # Combine the starting digits with the randomly generated digits
    random_number = start + remaining_digits
    return random_number


def generate_random_data():
    return generate_random_name(), generate_random_email(), generate_random_number()


test_data = [generate_random_data() for _ in range(5)]


# test function to fill the form
@pytest.mark.parametrize("name,email,phone", test_data)
def test_form_filling(driver, name, email, phone):
    driver.get("https://www.mindrisers.com.np/contact-us")
    driver.maximize_window()

    #scroll the window
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    target_y = 6000
    scroll_distance = 1000
    current_y = 0

    # looping concept as

    while current_y < target_y:
        driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
        current_y += scroll_distance
        time.sleep(0.25)

    # interact with web element as:
    name_field = driver.find_element(*(By.XPATH, "//input[@placeholder='Name']"))
    email_field = driver.find_element(*(By.XPATH, "//input[@placeholder='Email']"))
    phone_field = driver.find_element(*(By.XPATH, "//input[@placeholder='Phone']"))
    time.sleep(3)

    # fill the form
    name_field.clear()
    name_field.send_keys(name)
    time.sleep(3)

    if is_valid_email(email):
        email_field.clear()
        email_field.send_keys(email)
    else:
        print("invalid Email")
    time.sleep(3)
    phone_field.clear()
    phone_field.send_keys(phone)
    time.sleep(3)

    #print all the valuse for verification

    print(f"first_name:{name}")
    print(f"email:{email}")
    print(f"phone_number:{phone}")
