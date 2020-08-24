"""
@package utilities

CheckPoint class implementation
It provides functionality to assert the result

"""
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
from traceback import print_stack

class TestStatus(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        """
        Inits CheckPoint class
        """
        super(TestStatus, self).__init__(driver)
        self.resultList = []

    def setResult(self, result, resultMessage):
        try:
            if result is not None:
                if result:
                    self.resultList.append("PASS")
                    self.log.info("####Verification Successful :: " + resultMessage)
                else:
                    self.resultList.append("FAIL")
                    self.log.error("####Verification Failed ::" + resultMessage)
                    self.takeScreenshot(resultMessage)
            else:
                self.resultList.append("FAIL")
                self.log.error("####Verification Failed ::" + resultMessage)
                self.takeScreenshot(resultMessage)
        except:
            self.resultList.append("FAIL")
            self.log.error("Exception occured")
            self.takeScreenshot(resultMessage)
            print_stack()

    def mark(self, result, resultMessage):
        """
        mark the result of vaerification point in the testcase
        :param result: get result of the test
        :param message: get message to displayed
        :return: None
        """
        self.setResult(result, resultMessage)

    def markFinal(self, testName, result, resultMessage):
        """
        mark the final result of vaerification point in the testcase
        this should be called atleast once on testcase
        this should be final test status of the testcase
        :param result: get result of the test
        :param resultMessage: get message to displayed
        :return: None
        """
        self.setResult(result, resultMessage)

        if "FAIL" in self.resultList:
            self.log.error(testName + " ### TEST FAILED")
            self.resultList.clear()
            assert True == False
        else:
            self.log.info(testName + " ### TEST SUCCESSFUL")
            self.resultList.clear()
            assert True == True

