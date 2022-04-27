import os
import sys

import HtmlTestRunner

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

import unittest

from POM_Demo.Pages.LoginPage import LoginPage
from POM_Demo.Pages.HomePage import HomePage

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        #cls.driver=webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)

    def test_login_valid(self):
         self.driver.get("https://opensource-demo.orangehrmlive.com/")

         login = LoginPage(self.driver)
         login.enter_username("Admin")
         login.enter_password("admin123")
         login.click_login()

         homepage=HomePage(self.driver)
         homepage.click_welcome()
         homepage.click_logout()
         # self.driver.find_element(by=By.ID, value="txtUsername").send_keys("Admin")
         # self.driver.find_element(by=By.ID, value="txtPassword").send_keys("admin123")
         # self.driver.find_element(by=By.ID, value="btnLogin").click()
         # self.driver.find_element(by=By.ID, value="welcome").click()
         # self.driver.find_element(by=By.LINK_TEXT, value="Logout")
         time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")


if __name__ == '__main__':
     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="D:/my_world/PycharmProjects/POM_Demo/Reports"))