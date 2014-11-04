#!/usr/bin/env python
"""
Implementation of a min-heap data structure.
"""

class Heap:

    def __init__(self, list_=None):
        self._heap = [None]
        self._size = 0
        if list_ is not None:
            self.build_heap(list_)

    def build_heap(self, list_):
        """
        Produce a new heap from an unordered list.
        """
        self._heap = [None] + list_
        self._size = len(self._heap) - 1

        index = int(self._size / 2)
        while index >= 0:
            self._sift_down(index)
            index -= 1

    def size(self):
        """
        Return the size of the heap
        """
        return self._size

    def insert(self, val):
        """
        Insert an element into the heap.
        """
        self._heap.append(val)
        self._size += 1
        self._sift_up(self._size)

    def peek(self):
        """
        Return the root element.
        """
        return self._heap[1]

    def extract(self):
        """
        Return the root element and remove it from the heap.
        """
        if self._size < 1:
            return None

        root_value = self._heap[1]
        self._heap[1] = self._heap[self._size]
        self._heap.pop()
        self._size -= 1
        self._sift_down(1)
        return root_value

    def increase_key(self, index, value):
        """
        Increase the value of el's key to value
        """
        self._heap[index] = value

    def _sift_down(self, index):
        """
        Restore the heap property of the subtree at index.

        The element at index may or may not violate the property; it
        is assumed that the two child subtrees are both valid heaps.
        """
        heap = self._heap
        count = self._size
        left = index*2
        right = index*2 + 1
        swap = index

        if (left <= count and heap[left] <= heap[swap]):
            swap = left
        if (right <= count and heap[right] <= heap[swap]):
            swap = right

        if swap is not index:
            heap[index], heap[swap] = heap[swap], heap[index]
            self._sift_down(swap)

    def _sift_up(self, index):
        """
        Move index up the heap into a valid position.
        """
        parent = int(index/2)
        heap = self._heap
        if parent > 0 and heap[parent] > heap[index]:
            heap[parent], heap[index] = heap[index], heap[parent]
            self._sift_up(parent)





