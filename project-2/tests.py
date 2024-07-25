import unittest

from Mod import *

def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

class TestMod(unittest.TestCase):

    a = Mod(2, 3)
    b = Mod(5, 3)
    i = 7

    def setUp(self):
        pass


    def test_mod_equal(self):        
        self.assertEqual(self.a == self.b, True)

    def test_mod_not_equal(self):
        self.assertNotEqual(self.a, Mod(4, 3))

    def test_mod_add(self):
        self.assertEqual(self.a + self.b, Mod(7, 3))

    def test_mod_iadd(self):
        self.assertEqual(self.a + self.b, Mod(7, 3))

    def test_mod_sub(self):
        self.assertEqual(self.a - self.b, Mod(-3, 3))

    def test_mod_isub(self):
        self.assertEqual(self.a - self.b, Mod(-3, 3))

if __name__ == '__main__':
    run_tests(TestMod)