
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://tax.digitalpalika.org/login')

driver.maximize_window()
time.sleep(3)

driver.find_element(by=By.ID, value='username').send_keys('malikacounter5')
time.sleep(2)

driver.find_element(by=By.ID, value='password').send_keys('password')
time.sleep(2)

driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div/form/div[3]/button').click()
time.sleep(2)

print(driver.title)

driver.close()