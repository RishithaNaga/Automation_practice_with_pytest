
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import pytest
from selenium import webdriver
from pageObjects.signup_and_login_page import Login
from testcases import testcase_001_loginandsignup
from testcases.conftest import setup_and_teardown
from pageObjects.basePage import BasePage
from pageObjects.signup_and_login_page import Login
from utilities.customLogger import Loggen

@pytest.mark.usefixtures("setup_and_teardown")
class Test004_logout:
    logger=Loggen.mylog()

    def test_logout(self):
        self.logger.info("opening browser and navigating to url")
        BasePage_obj=BasePage(self.driver)
        signupandlogin_obj=Login(self.driver)
        self.logger.info("verifying home page")
        BasePage_obj.verify_homepage()
        self.driver.save_screenshot('C:\Automation_practice_with_pytest\Screenshots\homescreen.png')
        self.logger.info("clicking signup")
        BasePage_obj.click_signup_login()
        self.logger.info("entering login details")
        signupandlogin_obj.enterlogindetails("nagarishitha181292@gmail.com","Rishitha@1812")
        self.logger.info("verifying logged in as username")
        signupandlogin_obj.verify_loggedinasusername("Rishitha NagaRishitha Naga")
        self.driver.save_screenshot('C:\Automation_practice_with_pytest\Screenshots\loggedinaslogs.png')
        self.logger.info("click logout and verifying account login page")
        signupandlogin_obj.click_logout()
        signupandlogin_obj.verify_accountlogin_page()

