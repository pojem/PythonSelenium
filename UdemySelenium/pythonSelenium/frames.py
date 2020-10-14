from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

#iframe, frameset, frame
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")


driver.get("https://the-internet.herokuapp.com/iframe")

driver.switch_to.frame("mce_0_ifr") #frame ID

driver.find_element_by_css_selector("#tinymce").clear()
driver.find_element_by_css_selector("#tinymce").send_keys("Marko Komar")


#switch back to default content

driver.switch_to.default_content()

print(driver.find_element_by_tag_name("h3").text)

driver.close()