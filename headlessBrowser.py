from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager



options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.headless=False
options.add_argument('--incognito')


driver = webdriver.Chrome(options=options,service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10)

# options= webdriver.FirefoxOptions()
# options.headless=False
# options.add_argument('--incognito')

# driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))


driver.get('https://www.daraz.com.bd/')
print(driver.title)