from webbrowser import Chrome

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from Config.config import TestData
driver =None


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")
    parser.addoption("--username", action="store", help="input username")
    parser.addoption("--password", action="store", help="input password")
    parser.addoption("--firstname", action="store", help="input firstname")
    parser.addoption("--lastname", action="store", help="input lastname")
    parser.addoption("--email", action="store", help="input email")
    parser.addoption("--userdelete", action="store", help="input userdelete")
    parser.addoption("--departmentname", action="store", help="input deptname")

@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--ignore-certificate-error')
    if browser_name == "chrome":
        s = Service(TestData.chrome_executablepath)
        driver = webdriver.Chrome(service=s, options=chrome_options)
    elif browser_name == "firefox":
        s = Service(TestData.fireFox_executablepath)
        driver = webdriver.Firefox(service=s)

    driver.get(TestData.baseUrl)
    driver.maximize_window()
    request.cls.driver = driver
    yield


@pytest.fixture
def params(request):
    params = {}
    params['username'] = request.config.getoption('--username')
    params['password'] = request.config.getoption('--password')
    params['firstname'] = request.config.getoption('--firstname')
    params['lastname'] = request.config.getoption('--lastname')
    params['email'] = request.config.getoption('--email')
    params['userdelete'] = request.config.getoption('--userdelete')
    params['departmentname'] = request.config.getoption('--departmentname')
    if params['username'] is None and params['password'] is None:
        pytest.skip()
    return params



