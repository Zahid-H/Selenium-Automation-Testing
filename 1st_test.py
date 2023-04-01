import selenium

from selenium import webdriver

driver = webdriver.Chrome(executable_path="E:\chromedriver.exe")

driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
#for maximizing windows
# driver.maximize_window()
# #page title 
# print(driver.title)
# #for url print
# print(driver.current_url)
#locators(id,name,link_text,class_name,xpath)
#locator
# driver.find_element_by_id("name").send_keys("zahid Hasan")
# #now using action 
# driver.find_element_by_id("alertbtn").click()

#link text Automation click

driver.find_element_by_link_text("Free Access to InterviewQues/ResumeAssistance/Material").click()