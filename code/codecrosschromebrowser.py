from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(4)

driver.maximize_window()
driver.find_element(by=By.NAME,value="username").send_keys("Admin")
time.sleep(4)

driver.find_element(by=By.NAME,value="password").send_keys("Admin123")

driver.find_element(by=By.NAME,value="password").send_keys("Admin123")
driver.find_element(by=By.XPATH,value="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
exp_title = driver.title
act_title= "OrangeHRM"

if exp_title == act_title:
    (
        print("Test Successful")
    )

driver.close()