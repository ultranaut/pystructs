#!/usr/bin/env python
"""Implements a binary search tree."""

class Node:
    """A tree node."""
    def __init__(self, key, data=None):
        """Creates a node item."""
        self.key = key
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

class BinarySearchTree:
    """A binary search tree."""
    def __init__(self):
        """Creates an empty tree."""
        self._root = None

    def insert(self, key):
        """Insert a node into the tree."""
        new_node = Node(key)
        current_node = self._root

        if self._root is None:
            self._root = new_node
        else:
            while current_node and current_node is not new_node:
                if key < current_node.key:
                    if current_node.left is None:
                        new_node.parent = current_node
                        current_node.left = new_node
                    current_node = current_node.left
                else:
                    if current_node.right is None:
                        new_node.parent = current_node
                        current_node.right = new_node
                    current_node = current_node.right
            return new_node

    def _inorder(self, node, keys):
        if node:
            self._inorder(node.left, keys)
            keys.append(node.key)
            self._inorder(node.right, keys)

    def _preorder(self, node, keys):
        if node:
            keys.append(node.key)
            self._preorder(node.left, keys)
            self._preorder(node.right, keys)

    def _postorder(self, node, keys):
        if node:
            self._postorder(node.left, keys)
            self._postorder(node.right, keys)
            keys.append(node.key)

    def keys(self, order='in'):
        """Traverse the tree depth-first"""
        keys = []
        if order == 'in':
            self._inorder(self._root, keys)
        if order == 'pre':
            self._preorder(self._root, keys)
        if order == 'post':
            self._postorder(self._root, keys)
        return keys

    def get_min(self, node=None):
        if not node:
            node = self._root
        while node.left:
            node = node.left
        return node

    def get_max(self, node=None):
        if not node:
            node = self._root
        while node.right:
            node = node.right
        return node

    def find(self, key, node=None):
        if not node:
            node = self._root
        while node and node.key != key:
            if key < node.key:
                node = node.left
            else:
                node = node.right
        return node

    # def remove(self, node):
    #     # no children
    #     if not node.left and not node.right:
    #         if node.parent.right is node:
    #             node.parent.right = None
    #         else:
    #             node.parent.left = None
    #     if 
