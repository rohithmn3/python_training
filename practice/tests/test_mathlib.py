#!/usr/bin/python3

import unittest
import sys
sys.path.append('/home/rohithmn3/training_py/practice/other_lib')
import mathlib as m

class Mytest(unittest.TestCase):
    def setup(self):
        print("pre-req if any")
    def tearDown(self):
        print("destructor")
    def test_add(self):
        self.assertEqual(m.add(10,20),30)
        self.assertEqual(m.add(10,20),34)

if __name__ == "__main__":
    unittest.main()
