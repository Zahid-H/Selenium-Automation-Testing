import selenium
import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path="E:\chromedriver.exe")

driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

driver.find_element_by_xpath("//a[@id='opentab']").click()
tab = driver.window_handles[1]

driver.find_element_by_xpath("//button[@id='openwindow']").click()
windows2 = driver.window_handles[2]

driver.switch_to_window(tab)

driver.find_element_by_xpath("//div[@class='nav-outer clearfix']//nav[@class='main-menu']//div[@class='navbar-collapse collapse clearfix']//ul[@class='navigation clearfix']//li//a[@href='practice-project'][normalize-space()='Practice']").click()

driver.switch_to_window(windows2)