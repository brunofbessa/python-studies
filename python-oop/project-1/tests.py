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
        self.assertEqual(self.account_number, a.account_number)
        self.assertEqual(self.first_name, a.first_name)
        self.assertEqual(self.last_name, a.last_name)
        self.assertEqual(self.first_name+' '+self.last_name, a.full_name)
        self.assertEqual(self.tz, a.timezone)
        self.assertEqual(self.balance, a.balance)

    def test_create_account_empty_first_name(self):

        self.first_name = ''
        with self.assertRaises(ValueError):
            #expect to fail. If not raise the test fails
                a = self.create_account()

    def test_create_account_negative_balance(self):

        self.balance = -100.00
        with self.assertRaises(ValueError):
            #expect to fail. If not raise the test fails
                a = self.create_account()

    def test_create_account_withdraw_ok(self):

        withdraw_value = 20
        a = self.create_account()
        conf_code = a.withdraw(withdraw_value)
        self.assertEqual(conf_code[0], 'W')
        self.assertEqual(self.balance-withdraw_value, a.balance)

    def test_create_account_withdraw_rejected(self):

        withdraw_value = 1000
        a = self.create_account()
        conf_code = a.withdraw(withdraw_value)
        self.assertEqual(conf_code[0], 'R')
        self.assertEqual(self.balance, a.balance)

if __name__ == '__main__':
    run_tests(TestAccount)