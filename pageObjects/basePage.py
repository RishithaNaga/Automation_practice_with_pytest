from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException



class BasePage:

    button_home_xpath="//a[@href='/'])[2]"
    button_signup_login_xpath="//li/a[@href='/login']"
    button_products_xpath="//li/a[@href='/products']"
    button_cart_xpath="//li/a[@href='/view_cart']"
    button_testcases_xpath="//li/a[@href='/test_cases']"
    button_APItesting_xpath="//li/a[@href='/api_list']"
    button_videotutorials_xpath="//li/a[@href='https://www.youtube.com/c/AutomationExercise']"
    button_contactus_xpath="//li/a[@href='/contact_us']"
    text_homepage_xpath="//div[@class='brands_products']"
    text_successmsg_xpath="//*[contains(text(),'You have been successfully subscribed!')]"



    def __init__(self,driver):
        self.driver=driver

    def click_home(self):
        self.driver.click(By.XPATH,BasePage.button_home_xpath)

    def verify_homepage(self):
        if self.driver.find_element(By.XPATH,BasePage.text_homepage_xpath).is_displayed():
            print("Home page is visible")
        else:
            raise Exception("Home page is not visible")
    def click_signup_login(self):
        self.driver.find_element(By.XPATH,BasePage.button_signup_login_xpath).click()

    def click_products(self):
        self.driver.find_element(By.XPATH, BasePage.button_products_xpath).click()

    def click_cart(self):
        self.driver.click(By.XPATH, BasePage.button_cart_xpath)

    def click_testcases(self):
        self.driver.click(By.XPATH,BasePage.button_testcases_xpath)

    def click_APItesting(self):
        self.driver.find_element(By.XPATH, BasePage.button_APItesting_xpath).click

    def click_videotutorials(self):
        self.driver.find_element(By.XPATH, BasePage.button_videotutorials_xpath).click()

    def click_contactus(self):
        self.driver.find_element(By.XPATH, BasePage.button_contactus_xpath).click()

    def scrolltofooter(self):
        self.driver.scrolltoelement(By.XPATH,"//*[@class='footer-bottom']")

    def verify_subscription(self):
        actualtext="Subscription"
        expectedtext=self.driver.gettext(By.XPATH,"//*[@class='single-widget']/h2")
        print(expectedtext)
        if actualtext.casefold()==expectedtext.casefold():
            print("Subscription is visible")
        else:
            raise NoSuchElementException

    def enteremailandclick(self):
        self.driver.find_element(By.XPATH,"//*[@type='email']").send_keys("nagarishitha181292@gmail.com")
        self.driver.find_element(By.XPATH,"//*[@class='fa fa-arrow-circle-o-right']").click()

    def verifysuccessmsg(self):
        if self.driver.find_element(By.XPATH,BasePage.text_successmsg_xpath).is_displayed():
            print("success msg is printed")
        else:
            raise NoSuchElementException




