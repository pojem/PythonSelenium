from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

radio_buttons = driver.find_elements_by_class_name("radioButton")

print(len(radio_buttons))

radio_buttons[2].click()
assert radio_buttons[2].is_selected()

dropdown = Select(driver.find_element_by_id("dropdown-class-example"))
dropdown.select_by_visible_text("Option2")
#dropdown.select_by_index(0)

driver.close()