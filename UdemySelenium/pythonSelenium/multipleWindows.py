from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element_by_link_text("Click Here").click()

child = driver.window_handles[1]

driver.switch_to.window(child)

print(driver.find_element_by_tag_name("h3").text)
driver.close()

parent = driver.window_handles[0]
driver.switch_to.window(parent)
print(driver.find_element_by_tag_name("h3").text)

assert "Opening" in driver.find_element_by_tag_name("h3").text