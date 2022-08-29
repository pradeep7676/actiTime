from selenium.webdriver.common.by import By

from Pages.AddNewUsers import UserPage
from Utilities.BasePage import BasePage


class LoginPage(BasePage):
    '''LOCATORS'''
    USER_NAME = (By.ID, "username")
    PASSWORD = (By.CSS_SELECTOR , "input[name='pwd']")
    LOGIN_BUTTON = (By.ID, "loginButton")
    LOGOUT = (By.ID, "logoutLink")


    def __init__(self, driver):
        self.driver = driver

    def user_name(self):
        self.wait_presence(LoginPage.USER_NAME)
        return self.driver.find_element(*LoginPage.USER_NAME)

    def password(self):
        self.wait_presence(LoginPage.PASSWORD)
        return self.driver.find_element(*LoginPage.PASSWORD)

    def login_button(self):
        return self.driver.find_element(*LoginPage.LOGIN_BUTTON)

    def logout(self):
        self.wait_presence(LoginPage.LOGOUT)
        return self.driver.find_element(*LoginPage.LOGOUT)




