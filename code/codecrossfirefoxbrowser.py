import selenium
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import time

driver=webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("https://mindrisers.com.np/")
time.sleep(4)

driver.maximize_window()
time.sleep(4)

web_title=driver.title
print(f"Title={web_title}")



driver.close()