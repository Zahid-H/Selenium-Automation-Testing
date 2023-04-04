import selenium
import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="E:\chromedriver.exe")

driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

#form mouse to move to the hover button
action = ActionChains(driver)

action.move_to_element(driver.find_element_by_xpath("//button[@id='mousehover']")).perform()
time.sleep(2)
action.move_to_element(driver.find_element_by_xpath("//a[contains(text(),'Top')]")).click().perform()

