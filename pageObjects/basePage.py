from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from POMpractice.base_folder.config_file1 import BaseMethods

class BasePage:
    def __init__(self,driver):
        self.driver=driver

    def click_home(self):
        self.obj.click(By.XPATH,'(//a[@href="/"])[2]')

    def verify_homepage(self):
        if self.obj.isdisplayed(By.XPATH,"//div[@class='brands_products']"):
            print("Home page is visible")
        else:
            raise NoSuchElementException
    def click_signup_login(self):
        self.obj.click(By.XPATH,'//li/a[@href="/login"]')

    def click_products(self):
        self.obj.click(By.XPATH, '//li/a[@href="/products"]')

    def click_cart(self):
        self.obj.click(By.XPATH, '//li/a[@href="/view_cart"]')

    def click_testcases(self):
        self.obj.click(By.XPATH, '//li/a[@href="/test_cases"]')

    def click_APItesting(self):
        self.obj.click(By.XPATH, '//li/a[@href="/api_list"]')

    def click_videotutorials(self):
        self.obj.click(By.XPATH, '//li/a[@href="https://www.youtube.com/c/AutomationExercise"]')

    def click_contactus(self):
        self.obj.click(By.XPATH, '//li/a[@href="/contact_us"]')


    def scrolltofooter(self):
        self.obj.scrolltoelement(By.XPATH,"//*[@class='footer-bottom']")

    def verify_subscription(self):
        actualtext="Subscription"
        expectedtext=self.obj.gettext(By.XPATH,"//*[@class='single-widget']/h2")
        print(expectedtext)
        if actualtext.casefold()==expectedtext.casefold():
            print("Subscription is visible")
        else:
            raise NoSuchElementException

    def enteremailandclick(self):
        self.obj.sendkeys(By.XPATH,"//*[@type='email']","abc@gmail.com")
        self.obj.click(By.XPATH,"//*[@class='fa fa-arrow-circle-o-right']")

    def verifysuccessmsg(self):
        if self.obj.isdisplayed(By.XPATH,"//*[contains(text(),'You have been successfully subscribed!')]"):
            print("success msg is printed")
        else:
            raise NoSuchElementException




