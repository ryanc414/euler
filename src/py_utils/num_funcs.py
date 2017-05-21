#!/usr/bin/env python
"""Provides common functions related to integers."""
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


def gen_ints_of_len(length):
    """Generates all integers of a given length."""
    upper_limit = 10 ** length
    lower_limit = upper_limit // 10
    return range(lower_limit, upper_limit)

