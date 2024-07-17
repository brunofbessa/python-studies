import unittest
from datetime import timedelta, datetime

from Account import *
from TimeZone import *

def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

class TestAccount(unittest.TestCase):

    def setUp(self):
        self.account_number = 'A100'
        self.first_name = 'FIRST'
        self.last_name = 'LAST'
        self.tz = TimeZone('TZ', 1, 30)
        self.balance = 100.00
        self.withdraw_amount = 200

    def create_account(self):
        #self.setup_account()
        return Account(self.account_number, self.first_name, self.last_name, self.tz, self.balance)

    def test_create_timezone(self):
        tz = TimeZone('ABC', -1, -30)
        self.assertEqual('ABC', tz.name)
        self.assertEqual(timedelta(hours=-1, minutes=-30), tz.offset)

    def test_timezones_equal(self):
        tz1 = TimeZone('ABC', -1, -30)
        tz2 = TimeZone('ABC', -1, -30)
        self.assertEqual(tz1, tz2)

    def test_timezones_not_equal(self):
        tz = TimeZone('ABC', -1, -30)
        
        test_timezones = (
            TimeZone('DEF', -1, -30),
            TimeZone('ABC', -1, 30),
            TimeZone('ABC', 1, -30)
        )
        
        for test_tz in test_timezones:
            self.assertNotEqual(tz, test_tz)

    def test_create_account(self):

        a = self.create_account()
        #self.assertEqual(self.account_number, a.account_number)


if __name__ == '__main__':
    run_tests(TestAccount)