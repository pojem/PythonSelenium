from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
driver.get("https://login.salesforce.com/")

driver.find_element_by_css_selector("#username").send_keys("Marko")
driver.find_element_by_css_selector(".password").send_keys("Poje")
driver.find_element_by_css_selector(".password").clear() #clears Poje
driver.find_element_by_link_text("Forgot Your Password?").click()

driver.find_element_by_xpath("//a[text()='Cancel']").click()
print(driver.find_element_by_xpath("//div[@id='usernamegroup']/label").text)
print(driver.find_element_by_xpath("//form[@name='login']/div[1]/label").text)
print(driver.find_element_by_css_selector("form[name='login'] label:nth-child(3)").text)