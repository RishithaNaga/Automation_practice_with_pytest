
import sys
import os

import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from selenium import webdriver
from pageObjects.basePage import BasePage
from utilities.customLogger import Loggen
from pageObjects.signup_and_login_page import Login



@pytest.mark.usefixtures("setup_and_teardown")
class Test_005:

    logger=Loggen.mylog()
    def test_registerwithexistingemail(self):
        basepage_obj=BasePage(self.driver)
        signuppage_obj=Login(self.driver)
        self.logger.info("navigating to url")
        self.driver.get("https://automationexercise.com")
        self.logger.info("clicking on signup and login")
        basepage_obj.click_signup_login()
        self.logger.info("verifying new user signup")
        signuppage_obj.verify_newusersignup()
        self.logger.info("entering already registered username and email")
        signuppage_obj.enter_usernameandemail("Rishitha Naga","nagarishitha181292@gmail.com")
        self.logger.info("check if email already exists is displayed")
        self.driver.save_screenshot("C:\\Automation_practice_with_pytest\\Screenshots\\test005_registerwithexistingemail.png")



