from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import Select



options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=options,service=ChromeService(ChromeDriverManager().install()))

driver.get('https://www.orangehrm.com/en/book-a-free-demo/')


# def select_value_from_dropdown(dropDownList,value):
#  print(len(dropDownList))
# for ele in dropDownList:
#     print(ele.text)
#     if (ele.text=='Argentina'):
#         ele.click()
#         break
    
    # countryList =driver.find_elements(By.XPATH,'//select[@id="Form_getForm_Country"]/option')
    # select_value_from_dropdown(countryList,'Bangladesh')


countryDrop = driver.find_element(By.ID,'Form_getForm_Country')
# select =Select(countryDrop)

# Findout all country name from dropdown 
# ListCountry =select.options
# for ele in ListCountry:
#     print(ele.text)
    
    # when find bangladesh then break 
    # if(ele.text=='Bangladesh'):
    #     ele.click()
    #     break

# select.select_by_visible_text('Australia')
# select.select_by_value(5)
# select.select_by_value('Bangladesh')

# without Select method 
# countryList =driver.find_elements(By.XPATH,'//select[@id="Form_getForm_Country"]/option')
# print(len(countryList))
# for ele in countryList:
#     print(ele.text)
#     if (ele.text=='Argentina'):
#         ele.click()
#         break
    
    

