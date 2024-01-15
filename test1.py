from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Fix Selenium Browser Closes Automatically & 
# Immediately After Test Without Calling Quit or Close()
# below 2 lines 
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options,service=ChromeService(ChromeDriverManager().install()))
driver.get('https://web.facebook.com/mahtab.sentu')