
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))




from pageObjects.signup_and_login_page import Login
from utilities.customLogger import Loggen
import pytest


@pytest.mark.usefixtures("setup_and_teardown")
class Test_withincorrectlogin:
    logger = Loggen.mylog()

    def test_incorrectlogin(self):
        self.logger.info("********verifying login with incorrect credentials************")
        self.signupandloginobj = Login(self.driver)
        self.signupandloginobj.click_signupandlogin()
        self.signupandloginobj.enterlogindetails("nagarishitha181292@gmail.com", "Rishitha@181292")
        if self.signupandloginobj.display_error_msg():
            print("Invalid credentials")
        self.driver.save_screenshot("C:\\Automation_practice_with_pytest\\Screenshots\\screen003(1).png")
