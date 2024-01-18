from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=options,service=ChromeService(ChromeDriverManager().install()))

driver.get('https://www.amazon.in/')

# find multiple elements 

LinkList=driver.find_elements(By.TAG_NAME,'a')

# find total a tag 
print(len(LinkList))

for ele in LinkList:
 total_text = ele.text
print(total_text)
print(ele.get_attribute('href'))

from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=options,service=ChromeService(ChromeDriverManager().install()))

driver.get('https://www.amazon.in/')

# find multiple elements 

LinkList=driver.find_elements(By.TAG_NAME,'a')

# find total a tag 
print(len(LinkList))

for ele in LinkList:
 total_text = ele.text
print(total_text)
print(ele.get_attribute('href'))

ImageList=driver.find_elements(By.TAG_NAME,'img')
print(len(ImageList))


for ele in ImageList:
    print(ele.get_attribute('src'))





