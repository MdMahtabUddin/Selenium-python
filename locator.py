from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=options,service=ChromeService(ChromeDriverManager().install()))

driver.get('https://www.orangehrm.com/en/book-a-free-demo/')
# find element 
driver.find_element(By.ID,"Form_getForm_FullName").send_keys('Md Mahtab')
driver.find_element(By.ID,"Form_getForm_Email").send_keys("mahtab@open.com.bd")
driver.find_element(By.ID,"Form_getForm_CompanyName").send_keys("Open Communication")
driver.find_element(By.ID,"Form_getForm_Country").send_keys("Bangladesh")
driver.find_element(By.ID,"Form_getForm_Contact").send_keys("01671737845")

# menu iteams use link_text
driver.find_element(By.LINK_TEXT,"Solutions").click()
