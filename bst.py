#!/usr/bin/env python
"""Implements a binary search tree."""

class Node:
    """A tree node."""
    def __init__(self, key, value=None):
        """Creates a node item."""
        self._key = key
        self._val = value
        self._left = None
        self._right = None

    def show(self):
        print('Key:', self._key)
        print('Left:', self._left._key)
        print('Right:', self._right._key)

class BinarySearchTree:
    """A binary search tree."""
    def __init__(self):
        """Creates an empty tree."""
        self._root = None

    def insert(self, key):
        """Insert a node into the tree."""
        new_node = Node(key)

        if self._root is None:
            self._root = new_node
        else:
            current_node = self._root
            while True:
                parent = current_node
                if key < parent._key:
                    if not parent._left:
                        parent._left = new_node
                        break
                    else:
                        current_node = parent._left
                else:
                    if not parent._right:
                        parent._right = new_node
                        break
                    else:
                        current_node = parent._right
            return parent

    def _inorder(self, node, keys):
        if node != None:
            self._inorder(node._left, keys)
            keys.append(node._key)
            self._inorder(node._right, keys)

    def _preorder(self, node, keys):
        if node != None:
            keys.append(node._key)
            self._preorder(node._left, keys)
            self._preorder(node._right, keys)

    def _postorder(self, node, keys):
        if node != None:
            self._postorder(node._left, keys)
            self._postorder(node._right, keys)
            keys.append(node._key)

    def keys(self, order='in'):
        keys = []
        if order == 'in':
            self._inorder(self._root, keys)
        if order == 'pre':
            self._preorder(self._root, keys)
        if order == 'post':
            self._postorder(self._root, keys)
        return keys





