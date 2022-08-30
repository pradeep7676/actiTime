import logging

from selenium.webdriver.common.by import By
from Utilities.BasePage import BasePage
log = logging.getLogger(__name__)


class LoginPage(BasePage):
    """  LOCATORS"""
    USER_NAME = (By.ID, "username")
    PASSWORD = (By.CSS_SELECTOR, "input[name='pwd']")
    LOGIN_BUTTON = (By.ID, "loginButton")
    LOGOUT = (By.ID, "logoutLink")

    def __init__(self, driver):
        self.driver = driver

    def is_userName_present(self):
        if self.is_present(LoginPage.USER_NAME):
            log.info("present")

    def user_name(self):
        return self.driver.find_element(*LoginPage.USER_NAME)
    '''def user_name(self):
        if self.searchBox_is_present():
            self.wait_presence(LoginPage.USER_NAME)
            return self.driver.find_element(*LoginPage.USER_NAME)
        else:
            log.info("user input box is not present")'''

    '''def searchBox_is_present(self):
        search_box = self.driver.find_elements(*LoginPage.USER_NAME)
        searchBox = False
        if len(search_box) >= 1:
            searchBox = True
        return searchBox'''

    def is_password_input_present(self):
        if self.is_present(LoginPage.PASSWORD):
            log.info("present")

    def password(self):
        return self.driver.find_element(*LoginPage.PASSWORD)
    '''def password(self):
        if self.searchBox_is_passworD():
            self.wait_presence(LoginPage.PASSWORD)
            return self.driver.find_element(*LoginPage.PASSWORD)
        else:
            log.info("password input box is not present")'''

    '''def searchBox_is_password(self):
        search_box = self.driver.find_elements(*LoginPage.PASSWORD)
        searchBox = False
        if len(search_box) >= 1:
            searchBox = True
        return searchBox'''


    def login_button(self):
        return self.driver.find_element(*LoginPage.LOGIN_BUTTON)

    def logout(self):
        self.wait_presence(LoginPage.LOGOUT)
        return self.driver.find_element(*LoginPage.LOGOUT)
