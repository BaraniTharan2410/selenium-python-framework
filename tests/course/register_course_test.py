import unittest
from utilities.teststatus import TestStatus
import pytest
from pages.course.register_course_page import RegisterCoursePage

@pytest.mark.usefixtures("oneTimeSetup", "setUp")
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse= True)
    def objectSetup(self, oneTimeSetup):
        self.rc = RegisterCoursePage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order= 1)
    def test_EnrollCourse(self):
        result = self.rc.selectCourseToEnroll("JavaScript", "JavaScript for beginners")
        self.ts.markFinal("test_EnrollCourse", result, "Course enrolled successfully")



