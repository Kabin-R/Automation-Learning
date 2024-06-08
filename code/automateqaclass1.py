import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://mindrisers.com.np/contact-us')

driver.maximize_window()
time.sleep(5)

driver.find_element(by=By.NAME, value='name').send_keys('Kabin Rimal')
time.sleep(2)
driver.find_element(by=By.NAME, value='email').send_keys('Kabin@gmail.com')
time.sleep(2)

contact = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[2]/section[1]/div/form/div[2]/div[3]/input')
contact.send_keys('9845612389')
time.sleep(2)

subject = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[2]/section[1]/div/form/div[2]/div[4]/input')
subject.send_keys('QA')
time.sleep(2)

driver.find_element(by=By.NAME, value='message').send_keys('No')
time.sleep(3)

driver.find_element(by=By.XPATH, value='//*[@id="recaptcha-anchor"]/div[4]').click()
time.sleep(3)


Project_title = driver.title
print(f'The title is {Project_title}')

driver.close()
