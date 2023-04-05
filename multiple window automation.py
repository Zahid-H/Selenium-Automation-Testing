import selenium
import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="E:\chromedriver.exe")

driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

driver.find_element_by_xpath("//button[@id='openwindow']").click()
print(driver.window_handles)
#Switch to another window with window handler 
driver.switch_to_window(driver.window_handle[1])
driver.find_element_by_xpath("//li[@class='nav-item']//a[normalize-space()='Courses']").click()
driver.switch_to_window(driver.window_handle[0])