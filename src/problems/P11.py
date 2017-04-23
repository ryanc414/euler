#!/usr/bin/env python
"""
Find greatest product of four adjacent numbers in NxN grid
Usage: specify grid in plaintext file as command line arg
"""
from sys import argv


class CouldNotConvertInt(Exception):
    """
    Failure to convert input to integers.
    """


class OutOfRange(Exception):
    """
    Indices are out of the grid range.
    """


class Directions(object):
    """
    Methods for moving in a grid
    """
    def __init__(self, size):
        self.N = size

    def check_range(self, i, j):
        """
        Check if i, j are valid indices within the grid range
        """
        if i not in list(range(self.N)) or j not in list(range(self.N)):
            raise OutOfRange

    def right(self, i, j):
        """
        Move right in a grid
        """
        i += 1
        self.check_range(i, j)
        return i, j

    def right_down(self, i, j):
        """
        Move right-down in a grid
        """
        i += 1
        j += 1
        self.check_range(i, j)
        return i, j

    def down(self, i, j):
        """
        Move down in a grid
        """
        j += 1
        self.check_range(i, j)
        return i, j

    def left_down(self, i, j):
        """
        Move left-down in a grid
        """
        i -= 1
        j += 1
        self.check_range(i, j)
        return i, j

    def left(self, i, j):
        """
        Move left in a grid
        """
        i -= 1
        self.check_range(i, j)
        return i, j

    def left_up(self, i, j):
        """
        Move left-up in a grid
        """
        i -= 1
        j -= 1
        self.check_range(i, j)
        return i, j

    def up(self, i, j):
        """
        Move up in a grid
        """
        j -= 1
        self.check_range(i, j)
        return i, j

    def right_up(self, i, j):
        """
        Move right-up in a grid
        """
        i += 1
        j -= 1
        self.check_range(i, j)
        return i, j


class Grid(object):
    def __init__(self, gridfile):
        self.gridfile = gridfile
        self.grid = []
        self.maxproduct = 0
        self.N = 0

    @staticmethod
    def convert_line_to_int(line_list):
        """
        Converts a list of strings to a list of integers
        """
        try:
            int_list = [int(num) for num in line_list]
            return int_list
        except:
            raise CouldNotConvertInt(format(line_list))

    def read_gridfile(self):
        """
        Reads a grid from file into buffer.
        """
        with open(self.gridfile) as f:
            self.grid = [
                self.convert_line_to_int((line.strip()).split(' '))
                for line in f
                ]
        self.N = len(self.grid)

    def print_grid(self):
        """
        Prints a grid from file, for debugging purposes
        """
        print(self.N)
        for j in range(self.N):
            for i in range(self.N):
                print(self.element(i, j), end=' ')
            print('\n')

    def element(self, i, j):
        """
        Returns an element from the grid corresponding to the indices i, j
        """
        return (self.grid[j])[i]

    def find_product_of_four(self, i, j, increment):
        """
        Finds a prodduct of four consecutive numbers in the grid,
        using provided incrementer.
        Updates maxproduct if necessary.
        """
        n = 4
        product = 1
        for k in range(0, n):
            product *= self.element(i, j)
            (i, j) = increment(i, j)
        if product > self.maxproduct:
            self.maxproduct = product

    def find_all_products(self, i, j):
        """
        Finds all products starting from an arbitrary point in the grid.
        """
        directions = Directions(self.N)
        try:
            self.find_product_of_four(i, j, directions.right)
        except OutOfRange:
            pass
        try:
            self.find_product_of_four(i, j, directions.right_down)
        except OutOfRange:
            pass
        try:
            self.find_product_of_four(i, j, directions.down)
        except OutOfRange:
            pass
        try:
            self.find_product_of_four(i, j, directions.left_down)
        except OutOfRange:
            pass

    def iterate_over_elements(self):
        """
        Iterates over all grid elements an finds all products for each.
        Prints maximum product at end.
        """
        for i in range(0, self.N):
            for j in range(0, self.N):
                self.find_all_products(i, j)
        print("Max product is: {0}".format(self.maxproduct))

if __name__ == '__main__':
    try:
        mygrid = Grid(argv[1])
        mygrid.read_gridfile()
        mygrid.iterate_over_elements()
    except IndexError:
        print("Error: input grid file on command line.")
    except IOError:
        print("Error: could not read from file.")
    except CouldNotConvertInt:
        print("Error in converting input to integers.")

