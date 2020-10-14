from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
#driver.get("http://www.inisis.si/")
driver.implicitly_wait(5)

# MOVE TO ELEMENT *********************
action = ActionChains(driver)
#button = driver.find_element_by_id("menu-item-202")
#action.move_to_element(button).perform()
#action.move_to_element(driver.find_element_by_link_text("Titus")).click().perform()

# DOUBLE CLICK *************************

driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")

#button2 = driver.find_element_by_id("double-click")

#action.double_click(button2).perform()
#alert = driver.switch_to.alert

#print(alert.text)
#alert.accept()


menu = driver.find_element_by_id("sub-menu")
link = driver.find_element_by_id("link2")

action.move_to_element(menu).move_to_element(link).click().perform()

