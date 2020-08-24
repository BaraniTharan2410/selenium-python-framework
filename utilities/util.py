"""
@package utilities

all most commonly used utilities are implemented in the class
"""

import time
from traceback import print_stack
import random, string
import utilities.custom_logger as cl
import logging

class Util(object):

    log = cl.customLogger(logging.DEBUG)

    def sleep(self, sec):
        """
        put the test to wait for given amount of time
        :param sec: get seconds
        :return: None
        """
        try:
            time.sleep(sec)
            self.log.info("waiting for max ::" + str(sec) + "seconds")
        except InterruptedError:
            self.log.error("Exception occured during wait")
            print_stack()

    def getUniqueName(self, length= 10, type = "letters"):
        """
        Get unique string of characters
        :param length: Length of string or number of characters string should have
        :param type: Type of string should have. Default is letters
        :return: random unique string of characters
        """
        return self.getAlphanumeric(length)

    def getUniqueNameList(self, listSize= 5, itemList= None):
        """
        Get unique string of characters in list
        :param listSize: size of list
        :param length: Length of string or number of characters string should have
        :param type: Type of string should have. Default is letters
        :return: random unique string of characters
        """
        uniqueNameList = []
        for i in range(0, listSize):
            uniqueNameList.append(self.getAlphanumeric((itemList[i])))
        self.log.info("uniqueNameList are :" + uniqueNameList)
        return uniqueNameList

    def getAlphanumeric(self, length, type = "letters"):
        """
        Get random string of characters
        :param length: Length of string or number of characters string should have
        :param type: Provide lower/upper/digits for different types. Default is letters
        :return: random string of characters
        """
        alpha_num = ""
        if type == "digits":
            case = string.digits
        elif type == "lower":
            case = string.ascii_lowercase
        elif type == "upper":
            case = string.ascii_uppercase
        elif type == "mix":
            case = string.ascii_letters + string.digits
        else:
            case = string.ascii_letters
        result = alpha_num.join(random.choice(case) for i in range(length))
        self.log.info("Alpha numeric charceters are :" + result)
        return result

    def verifyListMatch(self, actual_list, expected_list):
        """
        verify the two given list matches
        :param actual_list: actual list
        :param expected_list: expected list
        :return: boolean
        """
        result= set(actual_list) == set(expected_list)
        self.log.info("Two given list match condition is  :" + result)
        return result

    def verifyListContains(self, actual_list, expected_list):
        """
        verify the values in actual list are present in expected list
        :param actual_list: actual list
        :param expected_list: expected list
        :return: boolean
        """
        result = False
        for i in range(0,len(actual_list)):
          if actual_list[i] in expected_list:
              result = True
          else:
              result =  False
        self.log.info("Two given list verify contain result is:" + result)
        return result