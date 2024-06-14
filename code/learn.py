import re
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://testautomationpractice.blogspot.com/')

driver.maximize_window()
time.sleep(4)

# Validation
def is_valid_email(email):
    try:
        email_pattern = "^[a-z]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"

        if re.search(email_pattern, email):
            return True

        else:
            return False

    except Exception as e:
        print("e")
        print(f"The email: {email} is invalid")


def is_valid_name(name):
    try:
        name_pattern = "^[a-z]+( [A-Z][a-z])?$"

        if re.match(name_pattern, name):
            return True
        else:
            return False

    except Exception as e:
        print(e)
        print(f"The name {name} is invalid")


def is_valid_phn(phn):
    try:
        phn_pattern = "^98\d{8}$"

        if re.match(phn_pattern, phn):
            return True
        else:
            return False

    except Exception as e:
        print(e)
        print(f"The number: {phn} is invalid")


#Generator
def rand_name_generator():
    name = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
    return name


def rand_email_generator():
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


name = rand_name_generator()
email = rand_email_generator()
phn = 9852364158
address = 'Nagarkot'

#Finding Elements in the page
name_field = driver.find_element(by=By.ID, value='name')
email_field = driver.find_element(by=By.ID, value='email')
phn_field = driver.find_element(by=By.ID, value='phone')
address_field = driver.find_element(by=By.ID, value='textarea')

#Assigning values
name_field.send_keys(name)
email_field.send_keys(email)
phn_field.send_keys(phn)
time.sleep(3)
address_field.send_keys(address)
time.sleep(2)

if is_valid_email(email):
    print("valid Email")
else:
    print(f"Invalid Email , {email}")

if is_valid_name(name):
    print("valid Name")
else:
    print(f"Invalid Name {name}")

driver.close()
