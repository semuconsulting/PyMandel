"""
Created on 3 May 2019

Test suite for PyMandel

@author: semuadmin
"""

import os
import sys
import unittest
from importlib import import_module

# inject local copy to avoid testing the installed version instead of the one in the repo
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
currdir = os.path.dirname(__file__)
import pymandel
import colormaps

print(f"Testing Local Version: {pymandel.version}")

# find files and the tests in them
mainsuite = unittest.TestSuite()
for modulename in [
    os.path.splitext(x)[0]
    for x in os.listdir(currdir or ".")
    if x != __file__ and x.startswith("test_") and x.endswith(".py")
]:
    try:
        module = import_module(modulename)
    except ImportError as err:
        print(f"skipping {modulename}, {err}")
    else:
        testsuite = unittest.findTestCases(module)
        print(f"found {testsuite.countTestCases()} tests in {modulename}")
        mainsuite.addTest(testsuite)

verbosity = 1
if "-v" in sys.argv[1:]:
    verbosity = 2
print("-" * 70)

# run the collected tests
testRunner = unittest.TextTestRunner(verbosity=verbosity)
# ~ testRunner = unittest.ConsoleTestRunner(verbosity=verbosity)
result = testRunner.run(mainsuite)

# set exit code accordingly to test results
sys.exit(not result.wasSuccessful())
