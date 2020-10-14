from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
#chrome_options.add_argument("headless") # this running chrome in background
chrome_options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe",options=chrome_options)
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_css_selector("a[href*='shop']").click()

products = driver.find_elements_by_xpath("//div[@class='card h-100']")

#//div[@class='card h-100']/div/h4/a
#//div[@class='card h-100']/div/button

for product in products:
    prduct_name = product.find_element_by_xpath("div/h4/a").text
    if prduct_name == "Blackberry":
        #add item to cart
        product.find_element_by_xpath("div/button").click()
        print("add item to cart")


wait = WebDriverWait(driver, 16)

driver.find_element_by_css_selector("a[class*='btn-primary']").click()
driver.find_element_by_css_selector("button[class*='btn-success']").click()
driver.find_element_by_id("country").send_keys("india")
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element_by_link_text("India").click()
driver.find_element_by_css_selector("input[type='submit']").click()
status = driver.find_element_by_css_selector("div[class*='alert-dismissible']").text

print(status)

assert "Success" in status

driver.get_screenshot_as_file("screen.png")