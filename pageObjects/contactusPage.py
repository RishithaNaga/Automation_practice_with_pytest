from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class contactus_page:

    text_username_xpath='//input[@type="text" and @name="name"]'
    text_usermail_xpath='//input[@type="email" and @name="email"]'
    text_subject_xpath='//input[@type="text" and @name="subject"]'
    text_message_xpath='//textarea[@id="message" and @name="message"]'
    message_getintouch_xpath='//h2[contains(text(),"Get In Touch")]'
    button_uploadfile_xpath='//input[@name="upload_file"]'
    button_submit_xpath='//input[@value="Submit"]'
    filepath=r"C:\Users\ssest\OneDrive\Desktop\CCL Appn.docx"
    message_success_xpath='(//div[contains(text(),"Success! Your details have been submitted successfully.")])[1]'

    def __init__(self,driver):
        self.driver=driver

    def enter_details(self,username,usermail,usersubject,usermsg):
        self.driver.find_element(By.XPATH,contactus_page.text_entername_xpath).send_keys(username)
        self.driver.find_element(By.XPATH,contactus_page.text_usermail_xpath).send_keys(usermail)
        self.driver.find_element(By.XPATH,contactus_page.text_subject_xpath).send_keys(usersubject)
        self.driver.find_element(By.XPATH,contactus_page.text_message_xpath).send_keys(usermsg)

    def verifygetintouch(self):
        if self.driver.isdisplayed(By.XPATH,contactus_page.message_getintouch_xpath):
            print("Get in touch is visible")
        else:
            raise NoSuchElementException

    def uploadfile(self):
        self.driver.find_element(By.XPATH,contactus_page.button_uploadfile_xpath).send_keys(contactus_page.filepath)
        self.driver.find_element(By.XPATH,contactus_page.button_submit_xpath).click()

    def click_ok(self):
        self.driver.switchto()

    def verifysuccessmsg(self):
        if self.driver.isdisplayed(By.XPATH,contactus_page.message_success_xpath):
            print("your details are entered successfully")
        else:
            raise NoSuchElementException



