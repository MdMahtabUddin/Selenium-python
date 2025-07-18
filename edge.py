from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time


options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)


driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

driver.get('https://www.google.com/')

time.sleep(30)
driver.quit()
