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
    driver.quit()


def test_google_search(driver):
    driver.get("https://www.google.com/")
    searchbar = driver.find_element(by=By.CSS_SELECTOR, value="textarea#APjFqb")
    searchbar.send_keys("mindrisers.com.np")
    searchbar.send_keys(Keys.RETURN)
    time.sleep(2)
    link = driver.find_element(*(By.CSS_SELECTOR, ".tF2Cxc > .yuRUbf .LC20lb"))
    link.click()
    time.sleep(3)
    print("\nCongratulation")
