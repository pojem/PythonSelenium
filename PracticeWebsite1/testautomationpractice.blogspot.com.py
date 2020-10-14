#Test whether the Home page has Three Sliders only

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait, Select
import re
#driver = webdriver.Firefox(executable_path="C:\Drivers\geckodriver.exe")
from selenium.webdriver.support.wait import WebDriverWait


# Test whether the Home page has Three Arrivals only
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
# self.driver.set_window_size(720, 1280)
driver.implicitly_wait(15)
driver.get("http://testautomationpractice.blogspot.com/")

aaa = driver.find_element_by_id("animals").text
