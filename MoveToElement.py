from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import Select
# move element 
from selenium.webdriver import ActionChains


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=options,service=ChromeService(ChromeDriverManager().install()))

driver.get('https://www.spicejet.com/')

# Move element

login_ele=driver.find_element(By.CSS_SELECTOR,"div.css-76zvg2.r-jwli3a.r-ubezar.r-16dba41.r-1pzd9i8")
act_chain =ActionChains(driver)
act_chain.move_to_element(login_ele).perform()

travel_agent= driver.find_element(By.LINK_TEXT,"Visa Services")
act_chain.move_to_element(travel_agent).perform()





