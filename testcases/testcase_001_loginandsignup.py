
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



import pytest
from selenium import webdriver
from pageObjects.signup_and_login_page import Login
from utilities.customLogger import Loggen


@pytest.mark.usefixtures("setup_and_teardown")
class Test_signup:

    logger = Loggen.mylog()

    def test_signup(self,setup_and_teardown):

        self.logger.info("********Test case 001*********")
        self.logger.info("*********Verifying signup***************")
        self.signupandloginobj = Login(self.driver)
        self.signupandloginobj.click_signupandlogin()
        self.signupandloginobj.enter_usernameandemail("rishitha naga","nagarishitha181292@gmail.com")
        self.driver.save_screenshot("C:\\Automation_practice_with_pytest\\Screenshots\\screen1.png")


    def test_login(self,setup_and_teardown):
        self.logger.info("********verifying login************")
        self.signupandloginobj = Login(self.driver)
        self.signupandloginobj.click_signupandlogin()
        self.signupandloginobj.enterlogindetails("nagarishitha181292@gmail.com","Rishitha@1812")
        self.driver.save_screenshot("C:\\Automation_practice_with_pytest\\Screenshots\\screen2.png")



