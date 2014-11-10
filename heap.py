#!/usr/bin/env python
"""
Min- and max-heap data structures.
"""

class MinHeap:
    """
    Binary min heap.
    """
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
        while index > 0:
            self._sift_down(index)
            index -= 1

    def size(self):
        """
        Return the size of the heap
        """
        return self._size

    def insert(self, value):
        """
        Insert a new element into the heap.
        """
        self._heap.append(value)
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
        Increase the value of the key at a given index.
        """
        if value < self._heap[index]:
            # raise an exception?
            pass

        self._heap[index] = value
        self._sift_down(index)

    def decrease_key(self, index, value):
        """
        Increase the value of the key at a given index.
        """
        if value > self._heap[index]:
            # raise an exception?
            pass

        self._heap[index] = value
        self._sift_up(index)

    def _sift_down(self, index):
        """
        Restore the heap property of the subtree at index.

        The element at index may or may not violate the property; it
        is assumed that the two child subtrees are both valid heaps.
        """
        heap = self._heap

        swap = self._down_index(index)
        if swap is not index:
            heap[index], heap[swap] = heap[swap], heap[index]
            self._sift_down(swap)

    def _sift_up(self, index):
        """
        Move the key at index up the heap into a valid position.
        """
        parent = int(index / 2)
        heap = self._heap
        if self._is_bad_child(index, parent):
            heap[parent], heap[index] = heap[index], heap[parent]
            self._sift_up(parent)

    def _down_index(self, index):
        """
        Find the index of the smallest of the values among
        a node and its children.
        """
        heap, size, swap = self._heap, self._size, index
        left = index * 2
        right = left + 1

        if (left <= size and heap[left] <= heap[swap]):
            swap = left
        if (right <= size and heap[right] <= heap[swap]):
            swap = right
        return swap

    def _is_bad_child(self, index, parent):
        heap = self._heap
        return parent > 0 and heap[parent] > heap[index]


class MaxHeap(MinHeap):
    """
    Binary max heap.
    """
    # Same implementation as min heap, but with the increase/decrease
    # key and _sift_up and _sift_down logics reversed
    def increase_key(self, index, value):
        """
        Increase the value of the key at a given index.
        """
        if value < self._heap[index]:
            # raise an exception?
            pass

        self._heap[index] = value
        self._sift_up(index)

    def decrease_key(self, index, value):
        """
        Increase the value of the key at a given index.
        """
        if value > self._heap[index]:
            # raise an exception?
            pass

        self._heap[index] = value
        self._sift_down(index)

    def _down_index(self, index):
        """
        Find the index of the largest of the values among
        a node and its children.
        """
        heap, size, swap = self._heap, self._size, index
        left = index * 2
        right = left + 1

        if (left <= size and heap[left] >= heap[swap]):
            swap = left
        if (right <= size and heap[right] >= heap[swap]):
            swap = right
        return swap

    def _is_bad_child(self, index, parent):
        heap = self._heap
        return parent > 0 and heap[parent] < heap[index]



