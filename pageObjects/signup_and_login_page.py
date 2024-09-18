from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class Login:
    button_signupandlogin_xpath='//li/a[@href="/login"]'
    text_signupname_xpath="//input[@type='text' and @data-qa='signup-name']"
    text_signupmail_xpath='//input[@type="email" and @data-qa="signup-email"]'
    button_signup_xpath='//button[@type="submit" and @data-qa="signup-button"]'
    text_loginemail_xpath='//input[@placeholder="Email Address" and @data-qa="login-email"]'
    text_loginpassword_xpath='//input[@placeholder="Password" and @data-qa="login-password"]'
    button_login_xpath='//button[@class="btn btn-default" and @data-qa="login-button"]'
    button_newusersignup_partiallinktext="New User Signup!"


    def __init__(self,driver):
        self.driver=driver

    def click_signupandlogin(self):
        self.driver.find_element(By.XPATH,self.button_signupandlogin_xpath).click()
    def enter_usernameandemail(self,username,usermail):
        self.driver.find_element(By.XPATH,self.text_signupname_xpath).send_keys(username)
        self.driver.find_element(By.XPATH,self.text_signupmail_xpath).send_keys(usermail)
        self.driver.find_element(By.XPATH,self.button_signup_xpath).click()

    def enterlogindetails(self,email,password):
        self.driver.find_element(By.XPATH,self.text_loginemail_xpath).send_keys(email)
        self.driver.find_element(By.XPATH,self.text_loginpassword_xpath).send_keys(password)
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def display_error_msg(self):
        try:
            error_msg=self.driver.find_element(By.XPATH,"//p[text()='Your email or password is incorrect!']")
            error_msg.is_displayed()
            return "Yes"
        except NoSuchElementException:
            return "No"

    def click_logout(self):
        self.driver.find_element(By.XPATH,'//a[@href="/logout"]').click()




