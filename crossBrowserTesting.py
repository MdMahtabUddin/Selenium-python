from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService

# Fix Selenium Browser Closes Automatically & 
# Immediately After Test Without Calling Quit or Close()
# below 2 lines 
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


browserName ="firefox"

if browserName =="chrome":
    driver=webdriver.Chrome(options=options, service=ChromeService (ChromeDriverManager().install())) 
    
elif browserName =="firefox":
    driver=webdriver.Firefox(executable_path=GeckoDriverManager().install())
    
elif browserName =="safari":
    driver=webdriver.Safari()     
else:
    print('pass the cross browser name:'+ browserName)  
    
driver.implicitly_wait(5) 
driver.get("https://LinkedIn.com/login")