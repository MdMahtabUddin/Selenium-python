from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=options,service=ChromeService(ChromeDriverManager().install()))

driver.get('https://app.hubspot.com/login')
# driver.find_element(By.CSS_SELECTOR,"#username").send_keys('mahtab45')

# Using Class Name 

# driver.find_element(By.CLASS_NAME,"login-email").send_keys('mahtab.sentu')
# driver.find_element(By.CLASS_NAME,"login-password").send_keys('bd45')

# Using CSS Selector

# driver.find_element(By.CSS_SELECTOR,"input.form-control.private-form__control.login-email").send_keys('mahtab.sentu')
# driver.find_element(By.CSS_SELECTOR,"form-control private-form__control login-password m-bottom-3").send_keys('bd45')

# Using Xpath 

# driver.find_element(By.XPATH,"//input[@class='form-control private-form__control login-email']").send_keys('mahtab')
# driver.find_element(By.XPATH,"//input[@class='form-control private-form__control login-password m-bottom-3']").send_keys('bd45')

# Using Link text 

driver.find_element(By.LINK_TEXT,'Sign up').click()

# Using Partial Link Text

driver.find_element(By.PARTIAL_LINK_TEXT,'Sign in').click()
