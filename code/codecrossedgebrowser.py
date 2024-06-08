import selenium
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

driver=webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

driver.get("https://mindrisers.com.np/")
time.sleep(4)

driver.maximize_window()
time.sleep(4)

web_title=driver.title
print(f"Title={web_title}")



driver.close()
