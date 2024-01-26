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

driver.get('https://jqueryui.com/droppable/')
driver.implicitly_wait(16)

source =driver.find_element(By.ID,'draggable')
target =driver.find_element(By.ID,'droppable')

act_chain=ActionChains(driver)
act_chain.drag_and_drop(source,target).perform()


