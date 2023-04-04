import selenium
import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="E:\chromedriver.exe")

driver.get("https://the-internet.herokuapp.com/context_menu")

#form mouse to move to the hover button
action = ActionChains(driver)
#context click means RIght click of the mouse
action.context_click(driver.find_element_by_xpath("//div[@id='hot-spot']")).perform()

