#!/usr/bin/env python
"""Provides functions related to numbers."""
from math import sqrt


class Divisors(object):
    """Allows iteration through proper divisors of n"""
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        limit = sqrt(self.n)
        for i in range(1, int(limit) + 1):
            if self.n % i == 0:
                yield i
                if i != limit and i != 1:
                    yield int(self.n / i)


def sum_of_divisors(n):
    """Returns sum of all proper divisors of n"""
    sum = 0

    for divisor in Divisors(n):
        sum += divisor

    return sum

