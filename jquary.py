from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import Select



options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=options,service=ChromeService(ChromeDriverManager().install()))


# generic function
def select_value(optionList,value):
    for ele in dropList:
    print(ele.text)
    if (ele.text== value):
        ele.click()
        break
    


driver.get('https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/')
driver.find_element(By.ID,'justAnInputBox').click()

dropList= driver.find_elements(By.CSS_SELECTOR,'span.comboTreeItemTitle')
select_value(dropList,'choice 2')

# print(len(dropList))

# for ele in dropList:
#     print(ele.text)
#     if (ele.text=='choice 6 2 3'):
#         ele.click()
#         break


