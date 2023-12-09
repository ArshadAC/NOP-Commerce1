import time
from selenium import webdriver
from pageObjects.LoginPage import Loginpage
from utilities.readProperties import Readconfig
class Test_Login:

    url = Readconfig.geturl()
    email = Readconfig.getemail()
    password = Readconfig.getpassword()

    def test_addcustomer(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.lp = Loginpage(self.driver)
        time.sleep(5)
        # self.lp.Enter_Email('admin@yourstore.com')
        self.lp.Enter_Email(self.email)
        # self.lp.Enter_Password('admin')
        self.lp.Enter_Password(self.password)
        self.lp.Click_Login()
        time.sleep(2)
        if self.driver.title == "Dashboard / nopCommerce administration":
            print(self.driver.title)
            assert True
        else:
            print("Test Failed")
            assert False
        self.lp.Click_Customers()
        # time.sleep(2)
        self.lp.Click_Customers1()
        # time.sleep(2)
        self.lp.Click_Addnew()
        time.sleep(2)
        self.lp.Enternewemail('tushar123@gmail.com')
        self.lp.Enternewpassword('tushar123')
        self.lp.Enterfirstname('Tushar')
        self.lp.Enterlastname('kadam')
        self.lp.Clickgender('Male')
        self.lp.EnterDOB('10/10/1999')
        self.lp.EnterComapnyname('Flipkart')
        self.lp.ClickTax()
        self.lp.SetCustomerrole('Administrators')
        self.lp.Set_manager(1)
        time.sleep(5)
        self.lp.Clickonsave()
        time.sleep(5)
