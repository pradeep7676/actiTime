

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from Config.config import TestData



def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")
    parser.addoption("--userName", action="store", help="input userName")
    parser.addoption("--passWord", action="store", help="input passWord")
    parser.addoption("--firstName", action="store", help="input firstName")
    parser.addoption("--lastName", action="store", help="input lastName")
    parser.addoption("--email", action="store", help="input email")
    parser.addoption("--userDelete", action="store", help="input userDelete")

@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        service_obj = Service(TestData.chrome_executablePath)
        driver = webdriver.Chrome(service=service_obj)

        driver.get(TestData.BASE_URL)
        driver.maximize_window()

        request.cls.driver = driver
        yield
        #driver.close()

@pytest.fixture
def params(request):
    params={'userName': request.config.getoption('--userName'),'passWord': request.config.getoption('--passWord'),
            'firstName': request.config.getoption('--firstName'),'lastName': request.config.getoption('--firstName'),
            'email': request.config.getoption('--email'),'userDelete': request.config.getoption('--userDelete')}
    if params['userName'] is None and params['passWord'] is None:
        pytest.skip()
    return params



