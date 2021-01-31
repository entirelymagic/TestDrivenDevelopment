import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        """A setUp to create 2 employee objects to test on."""
        print('setUp')
        self.emp_1 = Employee('Corey', 'Shaffer', 50000)
        self.emp_2 = Employee('Sue', 'Smith', 60000)

    def tearDown(self):
        print('tearDown\n')

    def test_email(self):
        """
        A test that check if the email is accordingly with the users emails, and if
        will change, the email will change as well.
        """
        self.assertEqual(self.emp_1.email, 'Corey.Shaffer@email.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')

        self.emp_1.first_name = 'John'
        self.emp_2.last_name = 'Munteanu'

        self.assertEqual(self.emp_1.email, 'John.Shaffer@email.com')
        self.assertEqual(self.emp_2.email, 'Sue.Munteanu@email.com')

    def test_apply_raise(self):
        """A test for the apply_raise method."""
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            # check if the return value is correct.
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success!'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/CoreyShaffer/May')
            self.assertEqual(schedule, 'Success!')

            # check for bad response if no return value
            mocked_get.return_value.ok = False
            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/SueSmith/June')
            self.assertEqual(schedule, 'Bad Response!')

