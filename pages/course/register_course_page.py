import logging
from base.basepage import BasePage
import utilities.custom_logger as cl

class RegisterCoursePage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super(RegisterCoursePage, self).__init__(driver)
        self.driver = driver

    ##############
    ###Locators###
    ##############

    _search_box = "//div/input[@id = 'search']"
    _search_course = "//div/button[@class= 'find-course search-course']"
    # _course = "//a/div/h4[contains(text(), 'JavaScript for beginners')]"
    _course = "//div/h4[contains(@class,'dynamic-heading') and contains(text(),'{0}')]"
    _enroll_button = "//div/button[contains(text(), 'Enroll')]"

    ##########################
    ###Element interactions###
    ##########################

    def enterCourseToSearch(self, course):
        self.enterTextByXpath(self._search_box, course)

    def clickSearchIconCourse(self):
        self.clickByXpath(self._search_course)

    def clickOnCourse(self, fullCourseName):
        self.clickByXpath(self._course.format(fullCourseName))

    def clickOnEnroll(self):
        self.clickByXpath(self._enroll_button)

    def selectCourseToEnroll(self, course= "", fullCourseName= ""):
        self.enterCourseToSearch(course)
        self.clickSearchIconCourse()
        self.clickOnCourse(fullCourseName)
        result = self.isElementDisplayedByXpath(self._enroll_button)
        self.clickOnEnroll()
        return result
