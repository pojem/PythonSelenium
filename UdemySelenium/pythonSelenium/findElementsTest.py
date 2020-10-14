from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
driver.get("https://www.makemytrip.com/")

driver.find_element_by_id("fromCity").click()
driver.find_element_by_xpath("//input[@placeholder='From']").send_keys("d")
time.sleep(0.5)
driver.find_element_by_xpath("//input[@placeholder='From']").send_keys("e")
time.sleep(0.5)
driver.find_element_by_xpath("//input[@placeholder='From']").send_keys("l")

time.sleep(3)
#p[class*='blackText'] <--css all options
time.sleep(3)

cities = driver.find_elements_by_css_selector("p[class*='blackText']")

for city in cities:
    print(city.text)
    if city.text == "Deline, Canada":
        city.click()
        break

time.sleep(3)
print("*****************************")
driver.find_element_by_xpath("//p[contains(text(),'Mumbai, India')]").click()

driver.quit()