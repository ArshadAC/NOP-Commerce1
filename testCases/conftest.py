import time
import pytest
from selenium import webdriver

# @pytest.fixture
# def setup():
#     driver = webdriver.Edge()
#     driver.get("https://admin-demo.nopcommerce.com/admin/")
#     driver.maximize_window()
#     return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome Browser")

    elif browser == 'edge':
        driver = webdriver.Edge()
        print("Launching Edge Browser")

    elif browser == 'firefox':
        driver = webdriver.Firefox
        print("Launching Firefox Browser")

    else:
        driver = webdriver.Edge()

    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver

def pytest_metadata(metadata):
    metadata["Environment"] = "Test"
    metadata["Project_Name"] = "NOP Commerece"
    metadata["Module Name"] = "Employee"
    metadata["Tester"] = "Arshad"

    metadata.pop("Pltform",None)
    metadata.pop("Plugins",None)