import time

from Config.config import TestData
from Pages.AddNewUsers import UserPage
from Pages.DeletingUsers import DeleteUserPage
from Pages.LoginPage import LoginPage
from Pages.TaskPage import TaskPage
from Utilities.BasePage import BasePage


class Test_ActiTime(BasePage):
    def test_e2e(self, params):
        log = self.getLogger()
        self.driver.implicitly_wait(10)
        ''' To verify LoginPage '''
        title = self.driver.title
        assert title == TestData.LOGIN_PAGE_TITLE
        log.info("Successfully verified loginPage title")

        """ 
        TO ENTER USER NAME AND PASSWORD AND LOGIN
        """
        login_obj = LoginPage(self.driver)
        login_obj.user_name().clear()
        login_obj.user_name().send_keys(params['userName'])
        login_obj.password().clear()
        login_obj.password().send_keys(params['passWord'])
        login_obj.login_button().click()
        log.info("Successfully logged in to the application")

        """TO VERIFY HOME PAGE TITLE"""
        home_title = self.driver.title
        assert home_title == TestData.HOME_PAGE_TITLE
        log.info("successfully verified home page ")

        """
        TO CREATE NEW USER USING NAME,EMAIL,DEPARTMENT
        """
        userPage = UserPage(self.driver)
        userPage.users_icon().click()
        user = self.driver.title
        assert user == TestData.USER_PAGE_TITLE
        log.info("userpage title verified")
        userPage.new_user().click()
        time.sleep(1)
        userPage.first_name().clear()
        userPage.first_name().send_keys(params['firstName'])
        userPage.last_name().clear()
        userPage.last_name().send_keys(params['lastName'])
        userPage.email().clear()
        userPage.email().send_keys(params['email'])
        userPage.department().click()
        userPage.adding_to_depart().click()
        self.waiting_until_item_enabled(userPage.save_button())
        userPage.save_button().click()
        text = userPage.verify().text
        assert text in "created"
        log.info(" successfully verified is user created or not")
        userPage.close().click()
        log.info("Successfully added the new user")
        self.driver.get_screenshot_as_file('usercreated.png')

        """
        TO DELETE CREATED USER 
        """
        delete_user = DeleteUserPage(self.driver)
        delete_user.search_icon().click()
        delete_user.search_by_name().send_keys(params['userDelete'])
        delete_user.click_on_user().click()
        time.sleep(1)
        self.waiting_until_item_enabled(delete_user.delete_button())
        delete_user.delete_button().click()
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        assert alert_text == TestData.ALERT_TEXT
        alert.accept()
        log.info("successfully deleted the user")
        self.driver.get_screenshot_as_file('deleteUser.png')

        """
        TO CREATE NEW PROJECT
        """
        task_obj = TaskPage(self.driver)
        task_obj.task_icon().click()
        task_obj.add_new().click()
        task_obj.new_project().click()
        task_obj.project_name().send_keys(TestData.PROJECT_NAME)
        task_obj.customer().click()
        task_obj.select_customer().click()
        task_obj.task_name().send_keys(TestData.TASK_NAME)
        task_obj.create_project().click()
        log.info("project created successfully")
        self.driver.get_screenshot_as_file('projectcreate.png')

        """
        TO SEARCH PROJECT AND DELETE
        """
        task_obj.Search_project().send_keys(TestData.PROJECT_NAME)
        time.sleep(1)
        task_obj.click_on_task().click()
        time.sleep(1)
        task_obj.actions().click()
        time.sleep(3)
        self.waiting_until_item_enabled(task_obj.delete())
        task_obj.delete().click()
        #task_obj.delete_confirmation().click()
        log.info("task deleted")

        """ 
        TO LOGOUT FROM THE APPLICATION 
        """
        login_obj.logout().click()
        log.info("logout from the application successfully")


