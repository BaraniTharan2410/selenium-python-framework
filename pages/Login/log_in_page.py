import logging
from base.basepage import BasePage
import utilities.custom_logger as cl
from pages.course.register_course_page import RegisterCoursePage

class LoginPage1(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ##############
    ###Locators###
    ##############

    _sign_up_ = "//div/a/div[contains(text(),'Sign Up or Log In')]"
    _email_ = "//form/div/input[@name = 'email']"
    _password_ = "//div/input[@name = 'password']"
    _submit_ = "//div/input[@type= 'submit']"
    _validmessagepath_ = "//span[@class='dynamic-text help-block']"
    _invalidmessagepath_ = "//span[@class='dynamic-text help-bloc']"
    _user_settings_icon = "//div/button/img[@class ='zl-navbar-rhs-img ']"

    def getEmail(self, emailId):
        self.enterTextByXpath(self._email_,emailId)
        return LoginPage1(self.driver)

    def getPassword(self, password):
        self.enterTextByXpath(self._password_, password)
        return LoginPage1(self.driver)

    def clickSignup(self):
        self.clickByXpath(self._sign_up_)
        return LoginPage1(self.driver)

    def clickSubmit(self):
        self.clickByXpath(self._submit_)
        return RegisterCoursePage(self.driver)

    def login(self, emailId="", password=""):
        self.clickSignup()
        self.getEmail(emailId)
        self.getPassword(password)
        self.clickSubmit()




