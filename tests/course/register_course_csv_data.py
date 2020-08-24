import unittest
from utilities.teststatus import TestStatus
import pytest
from pages.course.register_course_page import RegisterCoursePage
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData
from pages.navigation.page_navigation import NavigatingToPage

@pytest.mark.usefixtures("oneTimeSetup", "setUp")
@ddt
class RegisterMultipleCoursesTestsCSVData(unittest.TestCase):

    @pytest.fixture(autouse= True)
    def objectSetup(self, oneTimeSetup):
        self.rc = RegisterCoursePage(self.driver)
        self.ts = TestStatus(self.driver)
        self.nav = NavigatingToPage(self.driver)

    def setUp(self):
        self.nav.navigateToAllCourse()

    @pytest.mark.run(order= 1)
    @data(*getCSVData("C:\\Users\\acer\\workspace_python\\amazon\\testdata.csv"))
    @unpack
    def test_EnrollCourse(self, course, fullCourseName):
        result = self.rc.selectCourseToEnroll(course, fullCourseName)
        self.ts.markFinal("test_EnrollCourse", result, "Course enrolled successfully")
