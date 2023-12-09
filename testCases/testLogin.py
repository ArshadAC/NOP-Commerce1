import time
from selenium import webdriver
from pageObjects.LoginPage import Loginpage
from utilities.readProperties import Readconfig
from utilities.Logger import LogGenerator
class Test_Login:

    url = Readconfig.geturl()
    email = Readconfig.getemail()
    password = Readconfig.getpassword()
    log = LogGenerator.loggen()

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.log.info("opening browser")
        self.lp = Loginpage(self.driver)
        time.sleep(5)
        # self.lp.Enter_Email('admin@yourstore.com')
        self.lp.Enter_Email(self.email)
        self.log.info("Enter Email ID--> " + self.email)
        # self.lp.Enter_Password('admin')
        self.lp.Enter_Password(self.password)
        self.log.info("Enter Password--> "+ self.password)
        self.lp.Click_Login()
        time.sleep(2)
        if self.driver.title == "Dashboard / nopCommerce administration":
            print(self.driver.title)
            self.lp.ClickLogout()
            self.log.info("Click on Logout")
            assert True
        else:
            print("Test Failed")
            assert False

    def test_login_01(self,setup):
        self.driver = setup
        self.driver.get(self.url)
        self.lp = Loginpage(self.driver)
        self.lp.Enter_Email("admin@yourstore.com")
        self.lp.Enter_Password("admin123")
        self.lp.Click_Login()
        if self.driver.title == "Dashboard / nopCommerce administration":
            self.driver.save_screenshot("E:\\Automation Project\\New NOP commerece\\Screenshots\\test_login_01_Passed.png")
            self.lp.ClickLogout()
            assert True
        else:
            print("Test Failed")
            assert False
