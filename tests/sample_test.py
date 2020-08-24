import pytest
import unittest
from utilities.teststatus import TestStatus
from pages.course.register_course_page import RegisterCoursePage
from pages.home.login_page import LoginPage

@pytest.mark.usefixtures("oneTimeSetup", "setUp")
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse= True)
    def objectSetup(self, oneTimeSetup):
        self.rc = RegisterCoursePage(self.driver)
        self.ts = TestStatus(self.driver)
        self.lp = LoginPage(self.driver)

    @pytest.mark.run(order= 1)
    def test_EnrollCourse(self, course= "JavaScript", fullCourseName= "JavaScript for beginners"):
        self.rc.clickSearchIconCourse()
        self.rc.enterCourseToSearch(course)
        self.rc.clickOnCourse(fullCourseName)
        result = RegisterCoursePage.isElementDisplayedByXpath(self._enroll_button)
        self.rc.clickOnEnroll()
        self.ts.markFinal("test_EnrollCourse", result, "Course enrolled successfully")