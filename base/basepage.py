"""
@package base

Base Page class implementation

It implement methods which are common to all the pages throughout the application
This class need to inherited to all the page classes
This should not be used creating object instances
"""
from base.selenium_driver import SeleniumDriver
from traceback import print_stack
from utilities.util import Util
import utilities.custom_logger as cl
import logging

class BasePage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super(BasePage, self).__init__(driver)
        self.util = Util
        self.driver = driver

    def getTittle(self):
        """
        Get the current web page title
        :return: tittle
        """
        try:
            tittle = self.driver.title
            self.log.info("Title of the webpage : "+tittle)
        except:
            self.log.error("Title of Web page cannot be fetched")
            print_stack()
        return tittle