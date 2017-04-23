#!/usr/bin/env python
"""
Provides a class that allows iteration through digits in a number.
"""


class IterableInt(object):
    """
    Provide iteration through an integer's digits, as well as direct access via
    the .digits property.
    Arithmetic functions which return integers remain iterable.
    """
    def __init__(self, n):
        self.n = n
        self.digits = [int(digit) for digit in str(n)]

    def __iter__(self):
        for digit in self.digits:
            yield digit

    def reverse_digits(self):
        n = self
        while n:
            yield n % 10
            n //= 10

    def __add__(self, other):
        return IterableInt(self.n + other)

    def __sub__(self, other):
        return IterableInt(self.n - other)

    def __mul__(self, other):
        return IterableInt(self.n * other)

    def __truediv(self, other):
        return IterableInt(self.n / other)

    def __floordiv__(self, other):
        return IterableInt(self.n // other)

    def __pow__(self, other):
        return IterableInt(self.n ** other)

    def __len__(self):
        return len(self.digits)

    def __repr__(self):
        return self.n

    def __str__(self):
        return str(self.n)

    def __bool__(self):
        return bool(self.n)
