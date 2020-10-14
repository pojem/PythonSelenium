from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

#Js DOM can access any elements on web page just like how selenium does
#Selenium have a method to execute javascript code in it


driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_name("name").send_keys("hello selenium")

print(driver.find_element_by_name("name").text) # Doesnt work in this case
#########################
print(driver.find_element_by_name("name").get_attribute("value")) # now it works!!!!!!!!!!

print(driver.execute_script('return document.getElementsByName("name")[0].value'))

shopBtn = driver.find_element_by_css_selector("a[href*='shop']")

driver.execute_script("arguments[0].click();",shopBtn)


###### SCROLL ######### ***************** SCROLL SCROLL

driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

#driver.quit()