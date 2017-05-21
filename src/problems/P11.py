#!/usr/bin/env python3
"""
Find greatest product of four adjacent numbers in NxN grid
Usage: specify grid in plaintext file as command line arg
"""
import sys
import numpy as np
import directions


def read_gridfile(gridfile, seperator=' '):
    """
    Reads a grid from file into buffer.
    """
    with open(gridfile) as f:
        file_contents = f.readlines()

    grid = [
        convert_line_to_int((line.strip()).split(seperator))
        for line in file_contents]
    rows = len(grid)
    columns = len(grid[0])

    # Sanity check that each row we've been given has the same number of
    # columns.
    for row in grid:
        assert len(row) == columns

    return P11Grid(grid)


def convert_line_to_int(line_list):
    """
    Converts a list of strings to a list of integers
    """
    try:
        int_list = [int(num) for num in line_list]
        return int_list
    except:
        raise ValueError(format(line_list))


class P11Grid(np.matrix):
    """
    Provides methods for finding the greatest product of four consecutive
    adjacent numbers in a grid.
    """
    def __init__(self, *args):
        self.maxproduct = 0
        super().__init__()

    def find_product_of_four(self, i, j, increment):
        """
        Finds a product of four consecutive numbers in the grid,
        using provided incrementer. Updates maxproduct if necessary.
        """
        n = 4
        product = 1
        for k in range(0, n):
            product *= self[i, j]
            (i, j) = increment(i, j)
        if product > self.maxproduct:
            self.maxproduct = product

    def find_all_products(self, i, j):
        """
        Finds all products starting from an arbitrary point in the grid.
        """
        try:
            self.find_product_of_four(i, j, directions.right)
        except IndexError:
            pass
        try:
            self.find_product_of_four(i, j, directions.right_down)
        except IndexError:
            pass
        try:
            self.find_product_of_four(i, j, directions.down)
        except IndexError:
            pass
        try:
            self.find_product_of_four(i, j, directions.left_down)
        except IndexError:
            pass

    def find_maximum_product(self):
        """
        Iterates over all grid elements an finds all products for each.
        Returrns the maximum product found.
        """
        for i in range(0, self.size):
            for j in range(0, self.size):
                self.find_all_products(i, j)
        return self.maxproduct


if __name__ == '__main__':
    try:
        mygrid = read_gridfile(sys.argv[1])
        print("Maximum product of four consecutive elements is {}"
              .format(mygrid.find_maximum_product()))
    except IndexError:
        print("Error: input grid file on command line.")
    except IOError:
        print("Error: could not read from file.")
    except ValueError:
        print("Error in converting input to integers.")

