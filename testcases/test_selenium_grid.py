import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
#
#
#
# class Test_Google:
#     def test_google(self):
#         # Specify the Hub URL (change to your actual Hub IP)
#         hub_url = "http://192.168.29.101:4444/wd/hub"
#         chrome_options = Options()
#         chrome_service = Service(ChromeDriverManager().install())
#
#         # Create a Remote WebDriver session with Chrome options
#         driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
#
#         driver.implicitly_wait(10)
#         # Open a webpage (Google in this case)
#         driver.get("http://www.google.com")
#
#         # Print the page title to verify the session worked
#         print(driver.title)
#
#         # Close the browser
#         driver.quit()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Set the options for Chrome browser
chrome_options = Options()
chrome_options.add_argument("--headless")  # Optional: Run browser in headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Create a WebDriver instance pointing to the Selenium Grid Hub
driver = webdriver.Remote(
    command_executor="http://192.168.29.101:4444/wd/hub",
    options=chrome_options
)

# Run your tests
class Test1:
    def test1(self):
        driver.get("https://www.google.com")
        WebDriverWait(self.driver, 10).until(EC.title_contains("Google"))
        print(driver.title)

# Quit the driver
# driver.quit()
