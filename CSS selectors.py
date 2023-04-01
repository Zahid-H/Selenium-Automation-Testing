import selenium

from selenium import webdriver

driver = webdriver.Chrome(executable_path="E:\chromedriver.exe")

driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

#tagname[attribute = ‘value’]
driver.find_element_by_css_selector("input[value='radio1']").click()



