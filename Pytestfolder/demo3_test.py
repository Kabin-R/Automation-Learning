import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    #yeild the webdriver instance
    yield driver
    #Close the driver instance
    driver.close()


@pytest.mark.parametrize("username,password", [
    ("admin", "admin123"),  #valid username and password
    ("unadmin", "unadmin123"),  #invalid username and password
    ("1", "bye"),  #invalid username and password
    ("wrong", "")  #invalid username and password
])
def test_login(driver, username, password):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    username_field = driver.find_element(by=By.NAME, value="username")
    password_field = driver.find_element(by=By.NAME, value="password")
    login_button = driver.find_element(by=By.XPATH, value="//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")
    username_field.send_keys(username)
    password_field.send_keys(password)
    time.sleep(3)
    login_button.click()

    time.sleep(2)
    current_url = driver.current_url
    if current_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index':
        print(f"\nLogin Successful with Username: {username} \n Password: {password}")

    else:
        print(f"\nUsername:{username} \n password:{password} is incorrect")
