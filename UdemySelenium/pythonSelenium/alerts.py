from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

ime = "Marko Poje"
driver.find_element_by_id("name").send_keys(ime)
driver.find_element_by_id("alertbtn").click()
status = driver.switch_to.alert.text
aaa = "Hello {}, share this practice page and share your knowledge".format(ime)

#assert status == aaa
assert ime in status
driver.switch_to.alert.accept()

driver.find_element_by_id("confirmbtn").click()
time.sleep(3)
driver.switch_to.alert.dismiss()

driver.close()