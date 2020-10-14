#Implicit wait
#Explicit wait
#pause the test for few seconds using time class

from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
driver.implicitly_wait(5)
#wait until 3 seconds if object is not displayed
#global wait
#1.5 second to reach next page execution will resume in 1.5 sec
#if object do not show up at all, then max time your test waits for 5 seconds
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(3)
count = (len(driver.find_elements_by_xpath("//div[@class='products']/div")))
print(count)
assert count == 3

buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")

for b in buttons:
    b.click()

driver.find_element_by_css_selector("[alt='Cart']").click()
driver.find_element_by_xpath("//button[(text()='PROCEED TO CHECKOUT')]").click()
time.sleep(3)
driver.find_element_by_css_selector("input.promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector("button.promoBtn").click()
#here error will occur

code = driver.find_element_by_css_selector("span.promoInfo").text
print(code)

assert "applied" in code

driver.close()