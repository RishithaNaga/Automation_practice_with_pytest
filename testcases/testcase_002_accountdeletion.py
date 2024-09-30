
import pytest
from selenium import webdriver
from pageObjects.signup_and_login_page import Login
from testcases import testcase_001_loginandsignup

@pytest.mark.usefixtures("setup_and_teardown")
class Test002_accountdeletion:

    def test_accountdeletion(self):
        self.signupandloginobj=Login(self.driver)
        self.signupandloginobj.click_signupandlogin()
        self.signupandloginobj.enterlogindetails("nagarishitha181292@gmail.com", "Rishitha@1812")
        self.driver.save_screenshot("C:\\Automation_practice_with_pytest\\Screenshots\\screen3.png")
        self.signupandloginobj.verify_loggedinasusername("Rishitha NagaRishitha Naga")
        self.signupandloginobj.click_deleteaccount()
        self.signupandloginobj.verify_accountisdeleted()

