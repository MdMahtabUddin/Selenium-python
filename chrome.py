from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
# Fix Selenium Browser Closes Automatically & 
# Immediately After Test Without Calling Quit or Close()
# below 2 lines 
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=options,service=ChromeService(ChromeDriverManager().install()))
driver.get('https://www.google.com/')

driver.find_element(By.NAME,"q").send_keys("Mahtab")

print(driver.title)

time.sleep(30)
driver.quit()



