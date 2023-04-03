#multiple checkbox with single xpath

import selenium

from selenium import webdriver

driver = webdriver.Chrome(executable_path="E:\chromedriver.exe")

driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")

for checkbox in checkboxes:
    if checkbox == checkboxes[1]:
      pass
else:
    checkbox.click()

print(len(checkboxes))