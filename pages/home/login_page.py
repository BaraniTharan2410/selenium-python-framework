import logging
from base.basepage import BasePage
import utilities.custom_logger as cl
from utilities.util import Util
from pages.course.register_course_page import RegisterCoursePage
from pages.navigation.page_navigation import NavigatingToPage
class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)
        self.driver = driver
        self.nav = NavigatingToPage(self.driver)

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
    _log_out = "//ul/li/a[@href ='/logout']"
    _fail_message = "//div/form/div/span[contains(text(),'Your username or password is invalid. Please try again.')]"

    def getEmail(self, emailId):
        self.enterTextByXpath(self._email_,emailId)

    def getPassword(self, password):
        self.enterTextByXpath(self._password_, password)

    def clickSignup(self):
        self.clickByXpath(self._sign_up_)

    def clickSubmit(self):
        self.clickByXpath(self._submit_)

    def loginViaSignup(self, emailId="", password=""):
        self.clickSignup()
        self.getEmail(emailId)
        self.getPassword(password)
        self.clickSubmit()

    def loginViaSignin(self, emailId="", password=""):
        self.nav.navigateToSignIn()
        self.getEmail(emailId)
        self.getPassword(password)
        self.clickSubmit()

    def verifyLoginTitle(self):
        actual_tittle = self.getTittle()
        expected_title = "Let's Kode It"
        if actual_tittle in expected_title:
            return True
        return False

    def verifyLoginSuccess(self):
        result = self.isElementPresentByXpath(self._user_settings_icon)
        return result

    def verifyLoginFail(self):
        self.threadSleep(10)
        result = self.isElementPresentByXpath(self._fail_message)
        return result

    def logout(self):
        self.nav.navigateToUserSettings()
        self.clickByXpath(self._log_out)


