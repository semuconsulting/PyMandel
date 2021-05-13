"""
Created on 3 Oct 2020

Static method tests for pymandel

@author: semuadmin
"""

import unittest

from pymandel.mandelbrot import hsv_to_rgb


class StaticTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testhsv2rgb(self):
        res = hsv_to_rgb(0.5, 0.2, 0.9)
        self.assertEqual(res, (183, 229, 229))


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
