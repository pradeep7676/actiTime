import inspect
import logging
import time

import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup","params")
class BasePage:

    def wait_presence(self, path):
        """
            This wait is WebDriverWait along with expected condition where
            this wait used to wait for whether element of given locator
            is present or not.If not then raise exception.
        """
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.presence_of_element_located(path))
        except Exception as e:
            self.log.info(f"{path} is not present to locate")
            raise e

    def wait_clickable(self, path):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(path))

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logging.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger

    def waiting_until_item_enabled(self, item, time_out=30, interval_unit=0.5):
        log = self.getLogger()
        end_time = time.time() + time_out
        log.info(f"{item} : is Waiting for Enable")
        while time.time() < end_time and not item.is_enabled():
            time.sleep(interval_unit)

        if time.time() > end_time:
            log.info(f"{item} : is not enable error")
            raise TimeoutError()