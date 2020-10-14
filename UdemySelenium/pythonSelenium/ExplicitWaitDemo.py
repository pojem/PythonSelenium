#Implicit wait
#Explicit wait
#pause the test for few seconds using time class

from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(3)

lista1 = driver.find_elements_by_xpath("//h4[@class='product-name']")

aaa = []
bbb = []

for list in lista1:
    #print(list.text)
    aaa.append(list.text)

count = (len(driver.find_elements_by_xpath("//div[@class='products']/div")))
#print(count)
assert count == 3

buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")

for b in buttons:
    b.click()

driver.find_element_by_css_selector("[alt='Cart']").click()
driver.find_element_by_xpath("//button[(text()='PROCEED TO CHECKOUT')]").click()
time.sleep(3)

lista2 = driver.find_elements_by_xpath("//p[@class='product-name']")

for list2 in lista2:
    #print(list2.text)
    bbb.append(list2.text)

ccc = driver.find_element_by_css_selector("span.totAmt").text

driver.find_element_by_css_selector("input.promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector("button.promoBtn").click()
#here error will occur

#EXPLICITWAIT TARGET SPECIFIC ELEMENT
############################
wait = WebDriverWait(driver, 6)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"span.promoInfo")))
############################
code = driver.find_element_by_css_selector("span.promoInfo").text

ddd = driver.find_element_by_css_selector("span.discountAmt").text

print(ccc)
print(ddd)

e = int(driver.find_element_by_xpath("//tr[2]//td[5]/p").text)
f = int(driver.find_element_by_xpath("//tr[3]//td[5]/p").text)
g = int(driver.find_element_by_xpath("//tr[4]//td[5]/p").text)


amounts = driver.find_elements_by_xpath("//tr//td[5]/p")

sum=0
for amount in amounts:
    int(amount.text)
    sum = sum + int(amount.text)

total = int(driver.find_element_by_css_selector("span.totAmt").text)

assert "applied" in code and aaa == bbb and float(ddd) < float(ccc) and sum == total

driver.close()

#mentor@rahulshettyacademy.com