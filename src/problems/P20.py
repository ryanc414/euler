#!/usr/bin/env python
"""Factorial digit sum"""
from P16 import sum_digits
from math import factorial
from sys import argv, exit


def get_int_from_terminal():
    try:
        return int(argv[1])
    except IndexError:
        print "Error, specify N on command line."
    except ValueError:
        print "Error, N must be an integer."

if __name__ == '__main__':
    N = get_int_from_terminal()
    print sum_digits(factorial(N))
