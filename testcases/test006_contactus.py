# 1. Launch browser
# 2. Navigate to url 'http://automationexercise.com'
# 3. Verify that home page is visible successfully
# 4. Click on 'Contact Us' button
# 5. Verify 'GET IN TOUCH' is visible
# 6. Enter name, email, subject and message
# 7. Upload file
# 8. Click 'Submit' button
# 9. Click OK button
# 10. Verify success message 'Success! Your details have been submitted successfully.' is visible
# 11. Click 'Home' button and verify that landed to home page successfully

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import pytest
from utilities.customLogger import Loggen
from pageObjects.basePage import BasePage
from pageObjects.contactusPage import contactus_page


@pytest.mark.usefixtures("setup_and_teardown")
class Test_contactus:
    def test006_contactus(self):
        basepage_obj=BasePage(self.driver)
        contactuspage_obj=contactus_page(self.driver)
        logger=Loggen.mylog()
        logger.info("verifying home page")
        basepage_obj.verify_homepage()
        logger.info("click on ocntact us")
        basepage_obj.click_contactus()
        logger.info("verify get in touvh is displayed")
        contactuspage_obj.verifygetintouch()
        logger.info("enter user details")
        contactuspage_obj.enter_details("Rishitha","abc@gmail.com","hello","nothing")
        logger.info("upload a file")
        contactuspage_obj.uploadfile()
        logger.info("click on ok to proceed")
        contactuspage_obj.click_ok()
        logger.info("verify success message")
        contactuspage_obj.verifysuccessmsg()
        self.driver.save_screenshot("C:\\Automation_practice_with_pytest\\Screenshots\\test006_contactus.png")
        logger.info("click to navigate to home page")
        basepage_obj.click_home()
        logger.info("verify if home page is displayed")
        basepage_obj.verify_homepage()