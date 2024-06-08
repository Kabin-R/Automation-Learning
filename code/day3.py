import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://demo.nopcommerce.com/")
time.sleep(5)

driver.maximize_window()
driver.find_element(by=By.ID,value="customerCurrency").send_keys('Euro')
time.sleep(3)
