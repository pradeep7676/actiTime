from selenium.webdriver.common.by import By

from Utilities.BasePage import BasePage


class UserPage(BasePage):
    '''LOCATORS'''
    USER_ICON = (By.ID, "container_users")
    NEW_USER = (By.XPATH , "//div[@class='components_button withPlusIcon']")
    FIRST_NAME = (By.ID, "createUserPanel_firstNameField")
    LAST_NAME = (By.ID, "createUserPanel_lastNameField")
    EMAIL = (By.ID, "createUserPanel_emailField")
    DEPARTMENT = (By.XPATH, "//div[@class='simpleListMenuButton components_userGroupSelectorMenu emptyList notEmpty']")
    ADDING_TO_DEPARTMENT = (By.XPATH, "(//div[@class='item'])[2]")
    SAVE_BUTTON = (By.CSS_SELECTOR, "div[class='components_button submitBtn'] ")
    VERIFY = (By.CSS_SELECTOR, "div[class='createUserPanel_accountCreatedContainer'] div[class='invitationInfoHeader']")
    CLOSE_LINK = (By.XPATH, "//span[text()='Close']")

    def __init__(self, driver):
        self.driver = driver

    def users_icon(self):
        '''ADDING EXPLICIT WAIT'''
        self.wait_clickable(UserPage.USER_ICON)
        return self.driver.find_element(*UserPage.USER_ICON)

    def new_user(self):
        '''ADDING EXPLICIT WAIT'''
        self.wait_clickable(UserPage.NEW_USER)
        return self.driver.find_element(*UserPage.NEW_USER)

    def first_name(self):
        '''ADDING EXPLICIT WAIT'''
        self.wait_presence(UserPage.FIRST_NAME)
        return self.driver.find_element(*UserPage.FIRST_NAME)

    def last_name(self):
        '''ADDING EXPLICIT WAIT'''
        self.wait_presence(UserPage.LAST_NAME)
        return self.driver.find_element(*UserPage.LAST_NAME)

    def email(self):
        '''ADDING EXPLICIT WAIT'''
        self.wait_presence(UserPage.EMAIL)
        return self.driver.find_element(*UserPage.EMAIL)

    def department(self):
        '''ADDING EXPLICIT WAIT'''
        self.wait_clickable(UserPage.DEPARTMENT)
        return self.driver.find_element(*UserPage.DEPARTMENT)

    def adding_to_depart(self):
        '''ADDING EXPLICIT WAIT'''
        self.wait_clickable(UserPage.ADDING_TO_DEPARTMENT)
        return self.driver.find_element(*UserPage.ADDING_TO_DEPARTMENT)

    def save_button(self):
        '''ADDING EXPLICIT WAIT'''
        self.wait_clickable(UserPage.SAVE_BUTTON)
        return self.driver.find_element(*UserPage.SAVE_BUTTON)

    def verify(self):
        return self.driver.find_element(*UserPage.VERIFY)

    def close(self):
        return self.driver.find_element(*UserPage.CLOSE_LINK)




