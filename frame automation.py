import selenium
import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path="E:\chromedriver.exe")
driver.implicitly_wait(10)
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
#Selenium driver doesn't work for the fame elements so we need to swith to iframe

driver.switch_to_frame(driver.find_element_by_xpath("//iframe[@id='courses-iframe']"))
time.sleep(2)
driver.find_element_by_xpath("//div[@class='nav-outer clearfix']//nav[@class='main-menu']//div[@class='navbar-collapse collapse clearfix']//ul[@class='navigation clearfix']//li//a[@href='consulting'][normalize-space()='Job Support']").click()
