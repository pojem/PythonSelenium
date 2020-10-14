from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless") # this running chrome in background
chrome_options.add_argument("--ignore-certificate-errors")

# start the browser
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")
# chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--window-size=1920,1080")

#ref : https://www.programcreek.com/python/example/100025/selenium.webdriver.ChromeOptions

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe",options=chrome_options)

driver.get("https://rahulshettyacademy.com/angularpractice/")

print(driver.title)
driver.close