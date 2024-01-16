from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=options,service=ChromeService(ChromeDriverManager().install()))

driver.get('https://web.facebook.com/')
driver.find_element(By.NAME,"email").send_keys("mahtab.sentu@gmail.com")
driver.find_element(By.NAME,"pass").send_keys('#')
driver.find_element(By.XPATH,"//button[@value='1']").click()

