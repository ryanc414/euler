#!/usr/bin/env python
"""
Provides classes that allow iteration through digits in a number.
"""


class IterableInt(int):
    """
    Provide iteration through an integer's digits, as well as direct access via
    the .digits property.
    Arithmetic functions which return integers remain iterable.
    """
    def __init__(self, n):
        super(IterableInt, self).__init__(n)
        self.digits = list(self.reverse_digits())[::-1]

    def __iter__(self): 
        for digit in self.digits:
            yield digit


    def reverse_digits(self):
        n = self
        while n:
            yield n % 10
            n /= 10

    def __add__(self, other):
        return IterableInt(super(IterableInt, self).__add__(other))

    def __sub__(self, other):
        return IterableInt(super(IterableInt, self).__sub__(other))

    def __mul__(self, other):
        return IterableInt(super(IterableInt, self).__mul__(other))

    def __div__(self, other):
        return IterableInt(super(IterableInt, self).__div__(other))

    def __pow__(self, other):
        return IterableInt(super(IterableInt, self).__pow__(other))

    def __len__(self):
        return len(self.digits)

