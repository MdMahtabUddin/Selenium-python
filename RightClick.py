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



driver.get('https://swisnl.github.io/jQuery-contextMenu/demo.html')

right_click=driver.find_element(By.XPATH,"//span[text()='right click me']")
act_chans =ActionChains(driver)
act_chans.context_click(right_click).perform()

right_click_option = driver.find_elements(By.CSS_SELECTOR,'li.context-menu-item span')

for ele in right_click_option:
    print(ele.text)
    if(ele.text=='Paste'):
        ele.click()
        break
        

# driver.close()