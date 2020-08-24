import unittest
from tests.home.login_test import LoginTests
from tests.course.register_course_csv_data import RegisterMultipleCoursesTestsCSVData


#get test from all the classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(RegisterMultipleCoursesTestsCSVData)

#create test suite combining all the testcases
smoke_test = unittest.TestSuite([tc1, tc2])
unittest.TextTestRunner(verbosity=2).run(smoke_test)