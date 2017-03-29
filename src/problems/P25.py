#!/usr/bin/env python
"""1000-digit Fibonacci number"""

from math import log10
from fibonacci import FibonacciSeries

MAX_DIGITS = 1000


def main():
    """
    Iterate through Fibonacci numbers and print the term number of the first
    one to exceed MAX_DIGITS in length.
    """
    for term in FibonacciSeries():
        if log10(term.value) + 1 >= MAX_DIGITS:
            print((term.index))
            break


if __name__ == '__main__':
    main()

