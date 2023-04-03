import selenium
from selenium.webdriver.support.select import Select
import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="E:\chromedriver.exe")

driver.get("https://www.cleartrip.com/do/search/flights/")

driver.find_element_by_name("from").send_keys("Dha")
time.sleep(2)
from_airport= driver.find_elements_by_xpath("//ul[@id='ui-id-1']/li/div")

for airport in from_airport:
    if airport.text == "New York, US - All airports (NYC)":
        airport.click()
    else:
        pass

time.sleep(2)
driver.find_element_by_name("to").send_keys("New")
time.sleep(2)
to_airport= driver.find_elements_by_xpath("//ul[@id='ui-id-2']/li/div")

for air in to_airport:
    if air == "Dhaka, BD - Shahjalal Intl (DAC)":
        air.click()
    else:
        pass
