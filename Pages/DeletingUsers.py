from selenium.webdriver.common.by import By

from Utilities.BasePage import BasePage


class DeleteUserPage(BasePage):

    '''LOCATORS'''
    SEARCH_ICON = (By.XPATH, "//table[@class='userNameSelectorsTable']//div[@class='userList_wordsFilter']")
    SEARCH_BY_NAME = (By.CSS_SELECTOR,"div[class='inputPlaceholder animShowWordsField'] input[placeholder='Start typing name...']")
    CLICK_ON_USER = (By.XPATH, "//div[@class='name']/span/span")
    DELETE_BUTTON = (By.XPATH, "//div[@class='deleteButton actionButton']")

    def __init__(self, driver):
        self.driver = driver

    def search_icon(self):
        '''ADDING EXPLICIT WAIT'''
        self.wait_presence(DeleteUserPage.SEARCH_ICON)
        return self.driver.find_element(*DeleteUserPage.SEARCH_ICON)

    def search_by_name(self):
        '''ADDING EXPLICIT WAIT'''
        self.wait_presence(DeleteUserPage.SEARCH_BY_NAME)
        return self.driver.find_element(*DeleteUserPage.SEARCH_BY_NAME)

    def click_on_user(self):
        '''ADDING EXPLICIT WAIT'''
        self.wait_clickable(DeleteUserPage.SEARCH_ICON)
        return self.driver.find_element(*DeleteUserPage.CLICK_ON_USER)

    def delete_button(self):
        '''ADDING EXPLICIT WAIT'''
        self.wait_clickable(DeleteUserPage.SEARCH_ICON)
        return self.driver.find_element(*DeleteUserPage.DELETE_BUTTON)


