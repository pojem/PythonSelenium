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
driver.get("http://practice.automationtesting.in/")


class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("hahah")
        pass

    def test_1(self):
        print("test1")
        driver.find_element_by_xpath("//*[@id='menu-item-40']/a").click()
        driver.find_element_by_xpath("//*[@id='site-logo']/a/img").click()
        slider1 = driver.find_element_by_xpath("//*[@id='text-22-sub_row_1-0-2-0-0']/div/ul/li/a[1]/img").click()
        #driver.delete_all_cookies()
        self.assertTrue(True)

    def test_3(self):
        print("test3")
        driver.find_element_by_xpath("//*[@id='product-160']/div[3]/ul/li[1]/a").click()
        ccc=driver.find_element_by_xpath("//*[@id='tab-description']/p").text
        print(ccc)
        if "The Selenium WebDriver Recipes book" in ccc:
            print("PASS")
            y = True
        self.assertTrue(y)

    def test_4(self):
        print("test4")
        ddd=driver.find_element_by_xpath("//*[@id='product-160']/div[2]/p").text
        eee=int(ddd.split()[0])
        driver.find_element_by_xpath("//*[@id='product-160']/div[2]/form/div/input").send_keys(Keys.CONTROL,'a')
        driver.find_element_by_xpath("//*[@id='product-160']/div[2]/form/div/input").send_keys(Keys.BACKSPACE)
        driver.find_element_by_xpath("//*[@id='product-160']/div[2]/form/div/input").send_keys(str(eee-1))
        driver.find_element_by_xpath("//*[@id='product-160']/div[2]/form/button").click()
        driver.find_element_by_xpath("//*[@id='content']/div[1]/a").click()
        driver.find_element_by_id("coupon_code").send_keys("krishnasakinala")
        driver.find_element_by_name("apply_coupon").click()
        fff=driver.find_element_by_xpath("//*[@id='page-34']/div/div[1]/div[2]/div/table/tbody/tr[2]/td/span").text
        if fff == "haha":
            print("PASS"+fff)
        else:
            print("FAIL"+fff)
            z = False

        self.assertTrue(True)

    def test_5(self):
        print("test5")
        driver.find_element_by_xpath("//*[@id='page-34']/div/div[1]/form/table/tbody/tr[1]/td[1]/a").click()
        print("prišel sem do konca")
        #driver.close()
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()

