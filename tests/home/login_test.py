from pages.home.login_page import LoginPage
import pytest
import logging
import unittest
from utilities.teststatus import TestStatus
from pages.navigation.page_navigation import NavigatingToPage

@pytest.mark.usefixtures("oneTimeSetup","setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse= True)
    def classSetUp(self, oneTimeSetup):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.nav = NavigatingToPage(self.driver)

    @pytest.mark.run(order = 2)
    def test_validLogin(self):
        self.lp.loginViaSignin(emailId="test@email.com", password="abcabc")
        result1 = self.lp.verifyLoginTitle()
        self.ts.mark(result1, "Title verfication")
        result2 = self.lp.verifyLoginSuccess()
        self.ts.markFinal("test_validLogin", result2, "Login verfication")

    @pytest.mark.run(order = 1)
    def test_invalidLogin(self):
        self.lp.logout()
        self.lp.loginViaSignin(emailId="test@email.com", password="abcabcabc")
        result = self.lp.verifyLoginFail()
        assert result == True


