import pytest
from selenium import webdriver

@pytest.fixture(autouse=True)
def setup_and_teardown(request,browser):
    if browser=="Ie":
        driver=webdriver.Ie()
    elif browser=="Firefox":
        driver=webdriver.Firefox()
    else:
        driver=webdriver.Chrome()
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