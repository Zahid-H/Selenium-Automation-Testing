import selenium
import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="E:\chromedriver.exe")

driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")


driver.find_element_by_xpath("//input[@id='name']").send_keys("Zahid")
driver.find_element_by_xpath("//input[@id='confirmbtn']").click()
#We can not handle alert as it is  not the part of Html code that's why we switch to alert
popup = driver.switch_to_alert()

time.sleep(2)
# print(popup)
assert "Zahid" in popup.text
#this will dismiss the ok button in the pop up alert

popup.dismiss()



