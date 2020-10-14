from selenium import webdriver
from selenium.webdriver.support.select import Select

#driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
driver = webdriver.Firefox(executable_path="C:\Drivers\geckodriver.exe")

driver.get("https://rahulshettyacademy.com/angularpractice/")

#CSS STRUKTURA!!!

#    $("input[name='name']")
driver.find_element_by_css_selector("input[name='name']").send_keys("Marko")
driver.find_element_by_name("email").send_keys("abcd@ggg.com")

driver.find_element_by_id("exampleCheck1").click()

#select class provide the methods to handle the options in dropdown
dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)

#XPATH STRUKTURA!!!

#$x("//input[@type='submit']")

driver.find_element_by_xpath("//input[@class='btn btn-success']").click()

#print(driver.find_element_by_class_name("alert-success").text))
message = driver.find_element_by_xpath("//*[contains(@class,'alert-success')]").text
print(message)
assert "submitted" in message