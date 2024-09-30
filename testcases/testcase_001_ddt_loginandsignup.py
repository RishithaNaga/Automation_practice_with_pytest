import pytest
from selenium import webdriver
from pageObjects.signup_and_login_page import Login
from utilities.customLogger import Loggen
from utilities import excelUtilities
import datetime
import time
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

@pytest.mark.usefixtures("setup_and_teardown")
class Test_ddt_signup:
    logger = Loggen.mylog()
    file="C:/Automation_practice_with_pytest/TestData/TestData1.xlsx"
    current_time=datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')


    def test_login_ddt(self,setup_and_teardown):
        self.logger.info("********verifying login through data driven testing ************")
        self.signupandloginobj = Login(self.driver)
        rows=excelUtilities.getrowcount(self.file,"Sheet1")
        columns=excelUtilities.getcolumncount(self.file,"Sheet1")
        my_list=[]

        for r in range(2,rows+1):
            usermail=excelUtilities.readdata(self.file,"Sheet1",r,1)
            password=excelUtilities.readdata(self.file,"Sheet1",r,2)
            exp_output=excelUtilities.readdata(self.file,"Sheet1",r,3)
            self.signupandloginobj.click_signupandlogin()
            self.signupandloginobj.enterlogindetails(usermail,password)
            time.sleep(4)
            if self.signupandloginobj.display_error_msg()=="Yes" and exp_output=="Pass":
                my_list.append("Fail")
                self.driver.save_screenshot(
                    "C:/Automation_practice_with_pytest/Screenshots/screenshot" + self.current_time + ".png")
            elif self.signupandloginobj.display_error_msg()=="Yes" and exp_output=="Fail":
                my_list.append("Pass")
            elif self.signupandloginobj.display_error_msg()=="No" and exp_output=="Pass":
                my_list.append("Pass")
                self.signupandloginobj.click_logout()
            else:
                my_list.append("Fail")
                self.driver.save_screenshot(
                    "C:/Automation_practice_with_pytest/Screenshots/screenshot " + self.current_time + ".png")
                self.signupandloginobj.click_logout()
        print(my_list)
        if "Fail" in my_list:
            assert False
        else:
            assert True


