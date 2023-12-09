import time

import pytest

from pageObjects.LoginPage import Loginpage
from utilities import XLUtils
from utilities.Logger import LogGenerator
from utilities.readProperties import Readconfig

class Test_Login_DDT:

    url = Readconfig.geturl()
    log = LogGenerator.loggen()
    path ="E:\\Automation Project\\New NOP commerece\\testCases\\TestData\\LoginData.xlsx"

    def test_Login_DDT(self,setup):
        self.driver = setup
        self.log.info("test_Login_DDT_started")
        self.log.info("opening browser")
        self.driver.get(self.url)
        self.log.info("opening url-->" + self.url)
        self.lp = Loginpage(self.driver)
        self.rows = XLUtils.getrowCount(self.path,"Sheet1")
        print("Number of rows are ----" + str(self.rows))
        login_Status = []
        for r in range(2, self.rows + 1):
            self.email = XLUtils.readData(self.path, "Sheet1",r,2)
            self.password = XLUtils.readData(self.path, "Sheet1",r,3)
            self.exp_result =XLUtils.readData(self.path, "Sheet1",r,4)

            self.lp.Enter_Email(self.email)
            self.log.info("Entering Email--->" + self.email)
            self.lp.Enter_Password(self.password)
            self.log.info("Entering Password---->"+ self.password)
            self.lp.Click_Login()
            time.sleep(5)
            self.log.info("Click on Login")

            if self.driver.title == "Dashboard / nopCommerce administration":
                if self.exp_result == "Pass":
                    self.driver.save_screenshot("E:\\Automation Project\\New NOP commerece\\Screenshots\\test_DDT_Passed1.png")
                    self.lp.ClickLogout()
                    self.log.info("Click on Logout Button")
                    login_Status.append("Pass")
                    XLUtils.writeData(self.path,"Sheet1",r,5,"Pass")
                elif self.exp_result == "Fail":
                    self.driver.save_screenshot("E:\\Automation Project\\New NOP commerece\\Screenshots\\test_DDT_Failed1.png")
                    self.lp.ClickLogout()
                    self.log.info("Click on Logout Button")
                    login_Status.append("Fail")
                    XLUtils.writeData(self.path,"Sheet1",r,5,"Fail")
            else:
                if self.exp_result == "Pass":
                    login_Status.append("Fail")
                    self.driver.save_screenshot("E:\\Automation Project\\New NOP commerece\\Screenshots\\test_DDT_Filed2.png")
                    XLUtils.writeData(self.path,"Sheet1",r,5,"Fail")
                elif self.exp_result == "Fail":
                    self.driver.save_screenshot("E:\\Automation Project\\New NOP commerece\\Screenshots\\test_DDT_Passed2.png")
                    login_Status.append("Pass")
                    XLUtils.writeData(self.path,"Sheet1",r,5,"Pass")

        print(login_Status)
        if "Fail" not in login_Status:
            self.log.info("test_Login_DDT Passed")
            assert True
        else:
            self.log.info("test_Login_DDT Failed")
            assert False
        self.driver.close()
        self.log.info("test_Login_DDT completed")