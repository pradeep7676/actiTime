import time
from logging import getLogger

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.AddNewUsers import UserPage
from Pages.DeletingUsers import DeleteUserPage
from Pages.LoginPage import LoginPage
from Pages.TaskPage import TaskPage
from Utilities.BasePage import BasePage


class Test_Actitime(BasePage):
    def test_e2e(self, params):
        log = self.getLogger()
        self.driver.implicitly_wait(10)
        ''' To verify LoginPage '''
        title = self.driver.title
        assert title == TestData.LOGIN_PAGE_TITLE
        log.info("Successfully verified loginPage title")

        '''initialize Login page object'''
        login_obj = LoginPage(self.driver)

        '''Entering user name password to login'''
        login_obj.user_name().clear()
        login_obj.user_name().send_keys(params['username'])
        login_obj.password().clear()
        login_obj.password().send_keys(params['password'])
        login_obj.waiting_until_item_enabled( login_obj.login_button())
        login_obj.login_button().click()
        log.info("Successfully logged in to the application")

        '''to verify home page Title'''
        home_title = self.driver.title
        assert home_title == TestData.HOME_PAGE_TITLE
        log.info("successfully verified home page ")

        '''initialize UserPage object'''
        userPage = UserPage(self.driver)

        '''To click on users icon'''
        userPage.users_icon().click()

        '''To click on new user button'''
        user = self.driver.title
        assert user == TestData.USER_PAGE_TITLE
        log.info("userpage title verified")
        userPage.new_user().click()

        time.sleep(5)
        '''To enter first,last and email'''
        userPage.first_name().clear()
        userPage.first_name().send_keys(params['firstname'])
        userPage.last_name().clear()
        userPage.last_name().send_keys(params['lastname'])
        userPage.email().clear()
        userPage.email().send_keys(params['email'])

        '''To select which department'''
        userPage.department().click()
        userPage.adding_to_depart().click()

        '''To save new user'''
        self.waiting_until_item_enabled(userPage.save_button())
        userPage.save_button().click()
        text = userPage.verify().text
        assert text in "created"
        log.info(" successfully verified is user created or not")
        userPage.close().click()
        log.info("Successfully added the new user")

        '''initialize Delete user page object'''
        delete_user = DeleteUserPage(self.driver)

        '''To click on search icon'''
        delete_user.search_icon().click()

        '''To enter user name which we have to delete'''
        delete_user.search_by_name().send_keys(params['userdelete'])
        delete_user.click_on_user().click()
        time.sleep(4)

        '''to click on delete button'''
        self.waiting_until_item_enabled(delete_user.delete_button())
        delete_user.delete_button().click()

        '''to handle alert'''
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        assert alert_text == TestData.ALERT_TEXT
        alert.accept()
        log.info("successfully deleted the user")

        '''Initialize DepartmentPage object
        department_obj = DepartmentPage(self.driver)

        To click on department
        time.sleep(4)
        department_obj.click_on_department().click()

        To create new Departmen
        department_obj.add_department_name().send_keys(params['departmentname'])
        department_obj.add_department_name().send_keys(Keys.ENTER)
        time.sleep(4)
        #department_obj.delete_department().click()
        department_obj.close().click()
        #department_obj.delete_confirmation().click()
        log.info("Successfully deleted the department")'''

        task_obj = TaskPage(self.driver)
        #time.sleep(5)
        '''To click on task button'''
        task_obj.task_icon().click()

        '''To click on add new'''
        task_obj.add_new().click()

        '''to click on new project'''
        task_obj.new_project().click()

        '''to enter project name'''
        task_obj.project_name().send_keys("REDDY8")

        '''to select customer'''
        task_obj.customer().click()
        task_obj.select_customer().click()

        '''To enter task name'''
        task_obj.task_name().send_keys("login")
        self.waiting_until_item_enabled( task_obj.create_project())
        task_obj.create_project().click()
        log.info("project created successfully")

        '''TO search product delete it'''
        task_obj.Search_project().send_keys("REDDY8")
        time.sleep(5)
        task_obj.click_on_task().click()

        '''To click on action and delete button'''
        time.sleep(3)
        self.waiting_until_item_enabled(task_obj.actions())
        task_obj.actions().click()
        self.waiting_until_item_enabled(task_obj.delete())
        task_obj.delete().click()
        task_obj.scroll()
        task_obj.delete_confirmation().click()
        log.info("task deleted")

        login_obj.logout().click()
        time.sleep(5)
        log.info("logout from the application successfully")


