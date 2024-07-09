from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://mindrisers.com.np/blogs')

time.sleep(5)

#driver.find_element(by=By.ID , value='username').send_keys('Kabin Rimal')

#driver.find_element(by=By.XPATH , value='//*[@id = "subscribe"]').click()

#driver.find_element(by=By.XPATH , value="//*[@id = 'male']").click()

time.sleep(3)
driver.find_element(by=By.CSS_SELECTOR,
                    value=".container:nth-child(3)").click()
driver.maximize_window()
time.sleep(5)
Title = driver.title

print("The title is: ", Title)
