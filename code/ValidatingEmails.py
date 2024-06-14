import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
#Set up the Chrome WebDriver using WebDriver Manager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#define the function for valid email address

def is_valid_email(email):
    try:
        #check the formate using re(regular expression):
        email_pattern="^[a-z]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"

        if re.search(email_pattern, email):
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False

def is_valid_phone(phone):
    return bool(re.match(r'^\d{10}$',phone))

#open the website
driver.get("https://mindrisers.com.np/contact-us")

driver.maximize_window()

#set the scroll parameter

target_y=6000
scroll_distance=1000
current_y=0


#looping concept as

while current_y<target_y:
    driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
    current_y += scroll_distance
    time.sleep(0.25)

#interact with web element as:
name_field=driver.find_element((By.XPATH,"//input[@placeholder='Name']"))
email_field=driver.find_element((By.XPATH,"//input[@placeholder='Email']"))
phone_field=driver.find_element(*(By.XPATH,"//input[@placeholder='Phone']"))
time.sleep(3)

#fill the form
name="Ram"

email="ram@gmail.com"    #valid email

#invalid email
#email="ram@gmailcom"
#email="ram1232"
#email="ram@gmail"
#email="ram@gmail....com"

phone=""

time.sleep(3)
#check if name is empty:
if not name_field:
    print("Name cannot be empty")

#clear the field and pass the value:

name_field.send_keys(name)
time.sleep(2)

#check the validity of email address:
if is_valid_email(email):
    print("Email is valid:")
else:
    print("Email is invalid")

email_field.clear()
email_field.send_keys(email)
time.sleep(5)
#check the phone number field

if not phone:
    print("Phone cannot be empty")

#clear the field and send the value
phone_field.clear()
phone_field.send_keys(phone)

time.sleep(2)

driver.quit()
print("successfully code is execute!!")