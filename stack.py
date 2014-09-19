#!/usr/bin/env python
"""Implements a basic stack data structure.

Yes, it's a list.
"""

class Stack:

    def __init__(self):
        """Creates a new, empty stack object."""
        self._datastore = [];

    def push(self, item):
        """Pushes an item onto the end of the stack."""
        self._datastore.append(item)

    def pop(self):
        """Pops the top item off of the stack and returns it."""
        return self._datastore.pop()

    def top(self):
        """Returns the value of the item at the top of the stack."""
        return self._datastore[-1]

    def isempty(self):
        """Tests whether stack is empty."""
        return len(self._datastore) == 0

