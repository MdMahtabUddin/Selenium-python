from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=options,service=ChromeService(ChromeDriverManager().install()))

driver.get('https://classic.crmpro.com/')
driver.find_element(By.NAME,"username").send_keys("mahtab.sentu@gmail.com")
driver.find_element(By.NAME,"password").send_keys('Bangla@45#')
driver.find_element(By.XPATH,'//input[@value="Login"]').click()

