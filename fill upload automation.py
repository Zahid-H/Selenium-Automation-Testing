import selenium
import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="E:\chromedriver.exe")

driver.get("https://the-internet.herokuapp.com/upload")

driver.find_element_by_xpath("//input[@id='file-upload']").send_keys("C:\\Users\\Zahid\\Downloads\\Wall_TG.png")
time.sleep(2)
driver.find_element_by_xpath("//input[@id='file-submit']").click()

