import pytest
import unittest
from utilities.teststatus import TestStatus
from pages.course.register_course_page import RegisterCoursePage
from pages.Login.log_in_page import LoginPage1

@pytest.mark.usefixtures("oneTimeSetup", "setUp")
class RegisterCoursesTests(unittest.TestCase):

    # @pytest.fixture(autouse= True)
    # def objectSetup(self, oneTimeSetup):
    #     self.rc = RegisterCoursePage(self.driver)
    #     self.ts = TestStatus(self.driver)
    #     self.lp = LoginPage1(self.driver)

    @pytest.mark.run(order= 1)
    def test_searchCourse(self, emailId="test@email.com", password="abcabc",course="JavaScript"):
        LoginPage1(self.driver).\
        clickSignup().\
        getEmail(emailId).\
        getPassword(password).\
        clickSubmit().\
        enterCourseToSearch(course)