from selenium import webdriver

#here are the links for browser drivers https://www.selenium.dev/downloads/

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
#driver = webdriver.Firefox(executable_path="C:\Drivers\geckodriver.exe.exe")
#driver = webdriver.Ie(executable_path="C:\Drivers\IEDriverServer.exe") #PROBLEMS WITH SELENIUM FOR IE
#driver = webdriver.Edge(executable_path="C:\Drivers\msedgedriver.exe")

driver.maximize_window() #maximize window
driver.get("https://www.rahulshettyacademy.com/#/index")

print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.minimize_window() #minimize window
driver.back() #back button
driver.refresh() #refresh button
driver.quit()