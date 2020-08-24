import unittest
from utilities.teststatus import TestStatus
import pytest
from pages.course.register_course_page import RegisterCoursePage
from ddt import ddt, data, unpack


@pytest.mark.usefixtures("oneTimeSetup", "setUp")
@ddt
class RegisterMultipleCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse= True)
    def objectSetup(self, oneTimeSetup):
        self.rc = RegisterCoursePage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order= 1)
    @data(("JavaScript", "JavaScript for beginners"), ("Test Automation", "Complete Test Automation Bundle"),
          ("Selenium WebDriver","Selenium WebDriver With Python 3.x"))
    @unpack
    def test_EnrollCourse(self, course, fullCourseName):
        result = self.rc.selectCourseToEnroll(course, fullCourseName)
        self.ts.markFinal("test_EnrollCourse", result, "Course enrolled successfully")
        self.driver.find_element_by_link_text("ALL COURSES").click()