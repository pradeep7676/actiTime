import inspect
import logging
import time

import pytest
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
log = logging.getLogger(__name__)


@pytest.mark.usefixtures("setup", "params")
class BasePage:

    def wait_presence(self, path):
        """
            This wait is WebDriverWait along with expected condition where
            this wait used to wait for whether element of given locator
            is present or not.If not then raise exception.
        """
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(ec.presence_of_element_located(path))
        except Exception as e:
            log.info(f"{path} is not present to locate")
            raise e

    def wait_clickable(self, path):
        """
            This wait is WebDriverWait along with expected condition where
            this wait used to wait for whether element of given locator
            is clickable or not.If not then raise exception.The locator pass
            through from different page objects
        """
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(ec.element_to_be_clickable(path))
        except Exception as e:
            log.info(f"{path} is not clickable")
            raise e

    def wait_visibilityOfElementLocated(self, path):
        """
            This wait is WebDriverWait along with expected condition where
            this wait used to wait for whether element of given locator
            is clickable or not.If not then raise exception.The locator pass
            through from different page objects
        """
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(ec.invisibility_of_element(path))
        except Exception as e:
            log.info(f"{path} is not clickable")
            raise e

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logging.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger

    def is_present(self, path):
        """
            Method used to return search path enable or not """
        present = False
        if len(path) >= 1:
            present = True
        return present

    def waiting_until_item_enabled(self, item, time_out=30, interval_unit=0.5):
        end_time = time.time() + time_out
        log.info(f"{item} : is Waiting for Enable")
        while time.time() < end_time and not item.is_enabled():
            time.sleep(interval_unit)

        if time.time() > end_time:
            log.info(f"{item} : is not enable error")
            raise TimeoutError()
