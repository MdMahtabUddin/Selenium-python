from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=options,service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10)



driver.get('https://mail.rediff.com/cgi-bin/login.cgi')

driver.find_element(By.NAME,'proceed').click()
time.sleep(3)

# alert =driver.switch_to.alert
alert =driver.switch_to.default_content()
print(alert.text)
alert.accept()

# time.sleep(3)
# driver.quit()