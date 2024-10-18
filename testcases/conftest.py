import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(autouse=True)
def setup_and_teardown(request,browser):
    if browser=="Ie":
        driver=webdriver.Ie()
    elif browser=="Firefox":
        driver=webdriver.Firefox()
    else:
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Optional: Run browser in headless mode
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Remote(
            command_executor="http://192.168.29.101:4444/wd/hub",
            options=chrome_options
        )
        # driver=webdriver.Chrome()
    driver.get("https://automationexercise.com/")
    driver.maximize_window()
    request.cls.driver=driver
    yield driver
    driver.close()

def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

# def pytest_configure(config):
#     config._metadata['Projectname']='Automation Exercise'
#     config._metadata['Module name']='Customers'
#     config._metadata['Tester']='Rishitha'
#
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop('JAVA HOME',None)
#     metadata.pop('Plugins',None)