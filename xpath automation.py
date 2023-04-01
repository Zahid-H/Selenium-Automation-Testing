import selenium

from selenium import webdriver

driver = webdriver.Chrome(executable_path="E:\chromedriver.exe")

driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

#Xpath the most important locators
# //tagname[@attribute = ‘value’]
#<input> is tag name,@attribute is value, and ='value' is radio1
#driver.find_element_by_xpath("//input[@value='radio1']").click()
#//tagname[text() = ‘type text here’]

#for getting the name with Xpath
a= driver.find_element_by_xpath("//legend[text()='Checkbox Example']").text

print(a)
