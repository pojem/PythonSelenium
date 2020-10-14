from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxes = driver.find_elements_by_css_selector("input[type='checkbox']")

print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2": #get attribut >> returnes value of attribut
        checkbox.click()
        assert checkbox.is_selected()

driver.quit()