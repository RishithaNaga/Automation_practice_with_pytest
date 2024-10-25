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

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import pytest

from pageObjects.basePage import BasePage
from pageObjects.contactusPage import contactus_page


@pytest.mark.usefixtures("setup_and_teardown")
class Test_contactus:
    def test006_contactus(self):
        basepage_obj=BasePage(self.driver)
        contactuspage_obj=contactus_page(self.driver)

        basepage_obj.verify_homepage()
        basepage_obj.click_contactus()
        contactuspage_obj.verifygetintouch()
        contactuspage_obj.enter_details("Rishitha","abc@gmail.com","hello","nothing")
        contactuspage_obj.uploadfile()
        contactuspage_obj.click_ok()
        contactuspage_obj.verifysuccessmsg()
        basepage_obj.click_home()
        basepage_obj.verify_homepage()