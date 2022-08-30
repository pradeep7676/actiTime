from selenium.webdriver.common.by import By

from Utilities.BasePage import BasePage


class TaskPage(BasePage):
    '''LOCATORS'''
    TASK_ICON = (By.ID, "container_tasks")
    ADD_NEW = (By.XPATH, "//div[@class='addNewContainer']")
    NEW_PROJECT = (By.XPATH, "//div[@class='item createNewProject']")
    PROJECT_NAME = (By.CSS_SELECTOR, "input[class='projectNameField inputFieldWithPlaceholder inputNameField']")
    CUSTOMER = (By.CSS_SELECTOR, "div[class='comboboxButton']")
    SELECT_CUSTOMER = (By.XPATH, "//div[contains(@class,'itemRow cpItemRow')][normalize-space()='Big Bang Company']")
    TASK_NAME = (By.XPATH, "(//input[@placeholder='Enter task name'])[1]")
    CREATE_PROJECT = (By.CSS_SELECTOR, "div[class='components_button withPlusIcon']")
    SEARCHING_PROJECT = (By.XPATH, "(//input[@placeholder='Start typing name ...'])[1]")
    ''' CLICK_ON_TASK = (By.XPATH, "(//div[@class='namesContainer'])[1]")
    ACTIONS = (By.XPATH,"(//div[@class='action'][normalize-space()='ACTIONS'])[3]")
    DELETE = (By.XPATH, "(//div[@class='deleteButton'])[3]")
    DELETE_CONFIRMATION = (By.CSS_SELECTOR, "div[class='edit_task_sliding_panel sliding_panel components_panelContainer'] span[class='submitTitle buttonTitle']")'''
    CLICK_ON_TASK = (By.CSS_SELECTOR, "div[class='node projectNode editable selected'] div[class='editButton']")
    ACTIONS = (By.XPATH, "(//div[@class='action'][normalize-space()='ACTIONS'])[2]")
    DELETE = (By.XPATH, "(//div[@class='title'][normalize-space()='Delete'])[2]")
    DELETE_CONFIRMATION = (By.XPATH, "//div[@class='content_projectPanel']//div[@class='buttonIcon']")


    def __init__(self, driver):
        self.driver = driver

    def task_icon(self):
        self.wait_clickable(TaskPage.TASK_ICON)
        return self.driver.find_element(*TaskPage.TASK_ICON)

    def add_new(self):
        self.wait_clickable(TaskPage.ADD_NEW)
        return self.driver.find_element(*TaskPage.ADD_NEW)

    def new_project(self):
        self.wait_clickable(TaskPage.NEW_PROJECT)
        return self.driver.find_element(*TaskPage.NEW_PROJECT)

    def project_name(self):
        self.wait_presence(TaskPage.PROJECT_NAME)
        return self.driver.find_element(*TaskPage.PROJECT_NAME)

    def customer(self):
        self.wait_clickable(TaskPage.CUSTOMER)
        return self.driver.find_element(*TaskPage.CUSTOMER)

    def select_customer(self):
        self.wait_clickable(TaskPage.SELECT_CUSTOMER)
        return self.driver.find_element(*TaskPage.SELECT_CUSTOMER)

    def task_name(self):
        self.wait_presence(TaskPage.TASK_NAME)
        return self.driver.find_element(*TaskPage.TASK_NAME)

    def create_project(self):
        self.wait_presence(TaskPage.CREATE_PROJECT)
        return self.driver.find_element(*TaskPage.CREATE_PROJECT)

    def Search_project(self):
        self.wait_presence(TaskPage.SEARCHING_PROJECT)
        return self.driver.find_element(*TaskPage.SEARCHING_PROJECT)

    def click_on_task(self):
        self.wait_clickable(TaskPage.CLICK_ON_TASK)
        return self.driver.find_element(*TaskPage. CLICK_ON_TASK)

    def actions(self):
        self.wait_clickable(TaskPage.ACTIONS)
        return self.driver.find_element(*TaskPage.ACTIONS)

    def delete(self):
        self.wait_clickable(TaskPage.DELETE)
        return self.driver.find_element(*TaskPage.DELETE)

    def scroll(self):
        self.driver.execute_script("window.scrollTo(0,500);")

    def delete_confirmation(self):
       # self.wait_clickable(TaskPage.DELETE_CONFIRMATION)
        return self.driver.find_element(*TaskPage.DELETE_CONFIRMATION)








