#!/usr/bin/env python

import unittest
import bst
import random


class test_bst(unittest.TestCase):
    def setUp(self):
        self.bst = bst.BinarySearchTree()
        self.keys = ['h', 'c', 'a', 'e', 's', 'x', 'r']
        for key in self.keys[:]:
            self.bst.insert(key)
        self.keys.sort()

    def test_inorder(self):
        self.assertEqual(self.keys, self.bst.keys('in'))



# def setup(type='n'):
#     tree = bst.BinarySearchTree()
#     if type == 's':
#         tree.insert('h')
#         tree.insert('c')
#         tree.insert('a')
#         tree.insert('e')
#         tree.insert('s')
#         tree.insert('r')
#         tree.insert('x')
#     else:
#         tree.insert(23)
#         tree.insert(16)
#         tree.insert(22)
#         tree.insert(3)
#         tree.insert(45)
#         tree.insert(37)
#         tree.insert(99)

#     return tree

if __name__ == '__main__':
    unittest.main()
