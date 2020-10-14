from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

action = ActionChains(driver)

window = driver.find_element_by_id("displayed-text")
status = window.is_displayed()
print(status)

driver.find_element_by_id("hide-textbox").click()
status2 = window.is_displayed()

print(status2)

assert not status2 == True