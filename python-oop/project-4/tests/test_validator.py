#command line: python -m unittest tests/test_validator.py

import unittest

from app.models.validator import *

def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

class TestIntegerField(unittest.TestCase):

    class Person:
         age = IntegerField(0, 10)

    def test_set_age_ok(self):
        p = self.Person()
        p.age = 0
        self.assertEqual(0, p.age)

#overwrite class 

class TestIntegerField(unittest.TestCase):

    class Person:
        age = IntegerField(0, 10)

    def test_set_age_ok(self):
        min_ = 5
        max_ = 10
        self.Person.age = IntegerField(min_, max_)

        p = self.Person()
        p.age = min_
        self.assertEqual(min_, p.age)


if __name__ == '__main__':
    run_tests(TestIntegerField)