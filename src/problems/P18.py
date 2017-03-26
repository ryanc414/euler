#!/usr/bin/env python
"""Maximum path sum 1"""
from sys import argv


class NumberTriangle(object):
    """
    A number triangle is a triangular grid of numbers with each row having
    one more element than the previous.
    """
    def __init__(self, filename):
        self.filename = filename
        self.triangle = self.read_file()
        self.num_rows = len(self.triangle)
        self.path_lengths = [None for _ in range(self.num_rows)]

    def read_file(self):
        """Read a number triangle into memory"""
        with open(self.filename) as f:
            return [map(int, (line.strip()).split(' ')) for line in f]

    def find_largest_child(self, row, column):
        """Find the value of the largest child of a number in the triangle"""
        return max(
            self.path_lengths[row+1][column],
            self.path_lengths[row+1][column+1]
        )

    def find_largest_path(self):
        """
        Find the highest value path through the triangle, starting from the
        bottom.
        """
        self.path_lengths[self.num_rows-1] = self.triangle[self.num_rows-1]
        for row in range(self.num_rows - 1)[::-1]:
            self.path_lengths[row] = [
                (self.triangle[row][column] +
                 self.find_largest_child(row, column))
                for column in range(len(self.triangle[row]))
                ]
        print self.path_lengths[0][0]


if __name__ == '__main__':
    try:
        my_tri = NumberTriangle(argv[1])
    except IndexError:
        print "Error, specify number triangle filename on commandline."
    else:
        my_tri.find_largest_path()

