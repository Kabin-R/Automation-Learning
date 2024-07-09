import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_google_search():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.get("https://www.google.com/")
    searchbox = driver.find_element(by=By.CSS_SELECTOR, value="textarea#APjFqb")
    searchbox.send_keys("mindrisers.com.np")
    searchbox.send_keys(Keys.RETURN)
    time.sleep(2)
    link = driver.find_element(*(By.CSS_SELECTOR, ".tF2Cxc > .yuRUbf .LC20lb"))
    link.click()
    time.sleep(3)
    print("\nCongratulation")
