import unittest

from ProjectPOM.Pages.loginuda import loginuda
from selenium import webdriver

from selenium.webdriver.chrome.service import Service

class Loginuda(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        s = Service("D:/PyCharmProject/ProjectPom/chromedriver.exe")
        cls.driver = webdriver.Chrome(service=s)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_01(self):
        driver = self.driver

        driver.get("http://my.uda.edu.vn/sv/svlogin")
        Login = loginuda(driver)
        Login.enter_username("47756")
        Login.enter_Password("06/10/2001")
        Login.enter_Login()


        driver.save_screenshot("seve.png")

    @classmethod
    def tearDownClass(cls):
        # cls.driver.close()
        # cls.driver.quit()
        print('Hoàn Thành Kiểm Tra!')