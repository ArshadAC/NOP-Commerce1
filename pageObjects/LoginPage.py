import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
class Loginpage:
    Text_Email_XPATH = (By.XPATH,"//input[@id='Email']")
    Text_Password_XPATH = (By.XPATH,"//input[@id='Password']")
    Button_Login_XPATH = (By.XPATH,"//button[@type='submit']")
    Button_Customers_XPATH = (By.XPATH,"/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a")
    Button_Customers1_XPATH = (By.XPATH,"//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]")
    Button_Addnew_XPATH = (By.XPATH,"//a[@class='btn btn-primary']")
    Text_Newemail_XPATH = (By.XPATH,"//input[@id='Email']")
    Text_Newpassword_XPATH = (By.XPATH,"//input[@id='Password']")
    Text_Firstname_XPATH = (By.XPATH,"//input[@id='FirstName']")
    Text_Lastname_XPATH = (By.XPATH,"//input[@id='LastName']")
    RdButton_Gendermale_XPATH = (By.XPATH,"//label[@for='Gender_Male']")
    RdButton_GenderFemale_XPATH = (By.XPATH,"//label[@for='Gender_Female']")
    Text_DOB_XPATH = (By.XPATH,"//input[@id='DateOfBirth']")
    Text_Companyname_XPATH = (By.XPATH,"//input[@id='Company']")
    Button_Tax_XPATH = (By.XPATH,"//input[@id='IsTaxExempt']")
    Drp_Customerrole_XPATH = (By.XPATH,"//div[@class='input-group-append input-group-required']//div[@role='listbox']")
    List_Administrator_XPATH = (By.XPATH,"//option[normalize-space()='Administrators']")
    List_Forum_moderator_XPATH = (By.XPATH,"//option[normalize-space()='Forum Moderators']")
    List_Guests_XPATH = (By.XPATH,"//option[normalize-space()='Guests']")
    List_Registerd_XPATH = (By.XPATH,"//option[normalize-space()='Registered']")
    List_Vendor_XPATH = (By.XPATH,"//option[normalize-space()='Vendors']")
    Button_Save_XPATH = (By.XPATH,"//button[@name='save']//i[@class='far fa-save']")
    Drp_Managerofvendor_XPATH = (By.XPATH,"//select[@id='VendorId']")
    Btn_Logout_XPATH = (By.XPATH,"//a[normalize-space()='Logout']")
    def __init__(self,driver):
        self.driver = driver

    def Enter_Email(self, email):
        self.driver.find_element(*Loginpage.Text_Email_XPATH).clear()
        self.driver.find_element(*Loginpage.Text_Email_XPATH).send_keys(email)

    def Enter_Password(self, password):
        self.driver.find_element(*Loginpage.Text_Password_XPATH).clear()
        self.driver.find_element(*Loginpage.Text_Password_XPATH).send_keys(password)

    def Click_Login(self):
        self.driver.find_element(*Loginpage.Button_Login_XPATH).click()

    def Click_Customers(self):
        self.driver.find_element(*Loginpage.Button_Customers_XPATH).click()
        time.sleep(5)

    def Click_Customers1(self):
        self.driver.find_element(*Loginpage.Button_Customers1_XPATH).click()

    def Click_Addnew(self):
        self.driver.find_element(*Loginpage.Button_Addnew_XPATH).click()

    def Enternewemail(self,email):
        self.driver.find_element(*Loginpage.Text_Newemail_XPATH).send_keys(email)

    def Enternewpassword(self,password):
        self.driver.find_element(*Loginpage.Text_Newpassword_XPATH).send_keys(password)

    def Enterfirstname(self,firstname):
        self.driver.find_element(*Loginpage.Text_Firstname_XPATH).send_keys(firstname)

    def Enterlastname(self,lastname):
        self.driver.find_element(*Loginpage.Text_Lastname_XPATH).send_keys(lastname)

    def Clickgender(self,gender):
        if gender == 'Male':
            self.driver.find_element(*Loginpage.RdButton_Gendermale_XPATH).click()
        if gender == 'Female':
            self.driver.find_element(*Loginpage.RdButton_GenderFemale_XPATH).click()
        else:
            self.driver.find_element(*Loginpage.RdButton_Gendermale_XPATH).click()

    def EnterDOB(self,DOB):
        self.driver.find_element(*Loginpage.Text_DOB_XPATH).send_keys(DOB)

    def EnterComapnyname(self,company):
        self.driver.find_element(*Loginpage.Text_Companyname_XPATH).send_keys()

    def ClickTax(self):
        self.driver.find_element(*Loginpage.Button_Tax_XPATH).click()

    def SetCustomerrole(self,role):
        self.driver.find_element(*Loginpage.Drp_Customerrole_XPATH).click()
        time.sleep(2)
        if role == 'Administrators':
            self.driver.find_element(*Loginpage.List_Administrator_XPATH)
        if role == 'Forum Moderators':
            self.driver.find_element(*Loginpage.List_Forum_moderator_XPATH)
        if role == 'Guests':
            self.driver.find_element(*Loginpage.List_Guests_XPATH)
        if role == 'Registered':
            self.driver.find_element(*Loginpage.List_Registerd_XPATH)
        if role == 'Vendors':
            self.driver.find_element(*Loginpage.List_Vendor_XPATH)

    def Set_manager(self,value):
        drp = Select(self.driver.find_element(*Loginpage.Drp_Managerofvendor_XPATH))
        drp.select_by_index(value)
    def Clickonsave(self):
        self.driver.find_element(*Loginpage.Button_Save_XPATH).click()

    def ClickLogout(self):
        self.driver.find_element(*Loginpage.Btn_Logout_XPATH).click()