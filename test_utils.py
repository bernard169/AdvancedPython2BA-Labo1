# test_utils.py
# Author: Sébastien Combéfis
# Version: February 8, 2018

import unittest
import utils
import math

class TestUtils(unittest.TestCase):
    def test_fact(self):
        self.assertEqual (utils.fact(4),24)

    def test_roots(self):
        # À compléter...
        pass
    
    def test_integrate(self):
        self.assertEqual (utils.integrate ("x**2 - 1",2,4), 50/3) 

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
