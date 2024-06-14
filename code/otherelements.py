from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://demoqa.com/automation-practice-form")
time.sleep(4)

driver.maximize_window()

F_name = driver.find_element(by=By.ID,value='firstName')
L_name = driver.find_element(by=By.ID,value='firstName')

Email = driver.find_element(by=By.ID,value='userEmail')

Gender = driver.find_element(by=By.ID,value='gender-radio-1')

Mobile = driver.find_element()

DOB = driver.find_element()

Subject = driver.find_element()

Hobbies = driver.find_element()
