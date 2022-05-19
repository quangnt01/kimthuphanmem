from selenium.webdriver.common.by import By

from ProjectPOM.locators.location import Locators

class loginuda():

    def __init__(self,driver):
        self.driver = driver

        self.username_testbox_name = Locators.username_testbox_name
        self.Password_testbox_name = Locators.Password_testbox_name
        self.Login_button_id = Locators.Login_button_id


    def enter_username(self, username):
        self.driver.find_element(By.NAME, self.username_testbox_name).clear()
        self.driver.find_element(By.NAME, self.username_testbox_name).send_keys(username)

    def enter_Password(self, Password):
        self.driver.find_element(By.NAME, self.Password_testbox_name).clear()
        self.driver.find_element(By.NAME, self.Password_testbox_name).send_keys(Password)

    def enter_Login(self):
        self.driver.find_element(By.ID, self.Login_button_id).click()
