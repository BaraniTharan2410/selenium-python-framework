import logging
from base.basepage import BasePage
import utilities.custom_logger as cl
from pages.course.register_course_page import RegisterCoursePage

class NavigatingToPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super(NavigatingToPage, self).__init__(driver)
        self.driver = driver

    ##############
    ###Locators###
    ##############

    _my_course = "My COURSES"
    _all_courses = "All COURSES"
    _support = "SUPPORT"
    _home = "HOME"
    _user_settings_icon = "//div/button/img[@class ='zl-navbar-rhs-img ']"
    _sign_in = "SIGN IN"

    def navigateToMyCourse(self):
        self.clickByLinkText(self._my_course)

    def navigateToSignIn(self):
        self.clickByLinkText(self._sign_in)

    def navigateToAllCourse(self):
        self.clickByLinkText(self._all_courses)

    def navigateToSupport(self):
        self.clickByLinkText(self._support)

    def navigateToSupport(self):
        self.clickByLinkText(self._home)

    def navigateToUserSettings(self):
        self.clickByXpath(self._user_settings_icon)