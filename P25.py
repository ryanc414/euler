#!/usr/bin/env python
"""1000-digit Fibonacci number"""
from math import log10
from collections import namedtuple

MAX_DIGITS = 1000


class FibonacciNumbers(object):
    """
    Allows iteration through the Fibonnacci number series, starting with 1.
    Only the previous two terms are kept in memory.
    """
    def __init__(self, f_1=1, f_2=1):
        self.f_1 = f_1
        self.f_2 = f_2
        self.i = 1

    def __iter__(self):
        Term = namedtuple('Term', ['index', 'value'])
        yield Term(1, self.f_1)
        yield Term(2, self.f_2)
        i = 3
        while True:
            next_term = self.f_1 + self.f_2
            self.f_1 = self.f_2
            self.f_2 = next_term
            yield Term(i, next_term)
            i += 1


def main():
    """
    Iterate through Fibonacci numbers and print the term number of the first
    one to exceed MAX_DIGITS in length.
    """
    for term in FibonacciNumbers():
        if log10(term.value) + 1 >= MAX_DIGITS:
            print term.index
            break


if __name__ == '__main__':
    main()
