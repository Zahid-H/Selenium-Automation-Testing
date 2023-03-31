import selenium

from selenium import webdriver

driver = webdriver.Chrome(executable_path="E:\chromedriver.exe")

driver.get("https://www.google.com/")

driver.find_element_by_name("q").send_keys("Dhaka,Bangladesh")

driver.find_element_by_name("btnK").click()



