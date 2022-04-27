from selenium.webdriver.common.by import By

class HomePage():

    def __init__(self,driver):
        self.driver=driver

        self.welcome_link_id="welcome"
        self.logout_id="Logout"

    def click_welcome(self):
        self.driver.find_element(by=By.ID,value=self.welcome_link_id).click()

    def click_logout(self):
        self.driver.find_element(by=By.LINK_TEXT,value=self.logout_id).click()
