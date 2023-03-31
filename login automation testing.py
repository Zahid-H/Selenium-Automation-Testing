import selenium

from selenium import webdriver

driver = webdriver.Chrome(executable_path="E:\chromedriver.exe")

driver.get("https://practicetestautomation.com/practice-test-login/")


driver.find_element_by_id("username").send_keys("student")
#send keys for sending values in the text field
driver.find_element_by_name("password").send_keys("Password123")
#click is for performing actions 
driver.find_element_by_id("submit").click()


