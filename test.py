#!/usr/bin/env python

import unittest
import bst
import random

class test_bst(unittest.TestCase):
    def setUp(self):
        self.bst = bst.BinarySearchTree()
        self.keys = ['h', 'c', 'a', 'e', 's', 'r', 'x']
        for key in self.keys[:]:
            self.bst.insert(key)

    def test_order(self):
        self.assertEqual(sorted(self.keys), self.bst.keys('in'))
        self.assertEqual(self.keys, self.bst.keys('pre'))

if __name__ == '__main__':
    unittest.main()
