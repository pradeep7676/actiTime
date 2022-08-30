'''from selenium.webdriver.common.by import By

from Pages.AddNewUsers import UserPage
from Utilities.BasePage import BasePage


class DepartmentPage(BasePage):

    CLICK_ON_DEPARTMENT = (By.XPATH, "//div[@class='userList_manageButtons_component_manageGroupsButton']//div[contains(@class,'userList_manageButtons_component_groupItem department')][normalize-space()='Departments']")
    NEW_DEPARTMENT_NAME = (By.ID, "groupManagementLightBox_newGroupInput")
    TEXT1= (By.XPATH, "//table[@class='entityTable']/tr")
    DELETE_DEPARTMENT = (By.XPATH, "(//td[@class='deleteGroupCell'])[7] ")
    DELETE_CONFIRMATION = (By.XPATH, "(//button[@class='confirmDeleteGroupButton'])[6]")
    CLOSE = (By.ID, "groupManagementLightBox_closeLightbox")

    def __init__(self, driver):
        self.driver = driver

    def click_on_department(self):
        self.wait_clickable(DepartmentPage.CLICK_ON_DEPARTMENT)
        return self.driver.find_element(*DepartmentPage.CLICK_ON_DEPARTMENT)

    def add_department_name(self):
        self.wait_presence(DepartmentPage.NEW_DEPARTMENT_NAME)
        return self.driver.find_element(*DepartmentPage.NEW_DEPARTMENT_NAME)

    #def text1(self):
        #return self.driver.find_elements(*DepartmentPage.TEXT1)

    def delete_department(self):
        #self.wait_clickable(DepartmentPage.DELETE_DEPARTMENT)
        return self.driver.find_element(*DepartmentPage.DELETE_DEPARTMENT)

    def delete_confirmation(self):
        #self.wait_clickable(DepartmentPage.DELETE_CONFIRMATION)
        return self.driver.find_element(*DepartmentPage.DELETE_CONFIRMATION)

    def close(self):
        return self.driver.find_element(*DepartmentPage.CLOSE)'''