import selenium
import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path="E:\chromedriver.exe")

driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

get_attribute = driver.find_element_by_xpath("//input[@id='name']").get_attribute("placeholder")

print(get_attribute)