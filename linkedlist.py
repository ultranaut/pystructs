#!/usr/bin/env python
"""Totally slapped together singly linked list."""

class Node:
    def __init__(self, value):
        self.value = value
        self._next = None
    def show(self):
        return {'value': self.value, 'next': self._next}

class List:
    def __init__(self):
        self._list = None
        self._head = None
        self._tail = None

    def prepend(self, value):
        node = Node(value)
        node._next = self._head
        self._head = node

    def append(self, value):
        node = Node(value)
        if self._head is None:
            self._head = node
            self._tail = node
        else:
            self._tail._next = node
            self._tail = node
        return node

    def get(self):
        retval = []
        current_node = self._head
        while current_node:
            retval.append(current_node.value)
            current_node = current_node._next
        return retval

    def reverse(self):
        prev_node = None
        current_node = self._head
        self._tail = current_node

        while current_node:
            next_node = current_node._next
            current_node._next = prev_node
            prev_node = current_node
            current_node = next_node

        self._head = prev_node





