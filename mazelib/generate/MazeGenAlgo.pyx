
from __future__ import absolute_import
from mazelib.utils.MazeArray import MazeArray
from random import shuffle


cdef class MazeGenAlgo:

    def __cinit__(self, h, w):
        if w < 3 or h < 3:
            raise ValueError('A maze smaller than 3x3 is not a maze.')
        self.h = h
        self.w = w
        self.H = (2 * self.h) + 1
        self.W = (2 * self.w) + 1

    def __init__(self, h, w):
        pass

    def __dealloc__(self):
        pass

    cpdef object generate(self):
        return

    """
    All of the methods below this are helper methods,
    common to many maze-generating algorithms.
    """

    cpdef object _find_neighbors(self, posi, grid, is_wall=False):
        """Find all the grid neighbors of the current position;
        visited, or not.
        """
        cdef int r, c
        r, c = posi
        ns = []

        if r > 1 and grid[r-2, c] == is_wall:
            ns.append((r-2, c))
        if r < self.H-2 and grid[r+2, c] == is_wall:
            ns.append((r+2, c))
        if c > 1 and grid[r, c-2] == is_wall:
            ns.append((r, c-2))
        if c < self.W-2 and grid[r, c+2] == is_wall:
            ns.append((r, c+2))

        shuffle(ns)

        return ns
