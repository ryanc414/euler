#!/usr/bin/env python3
"""Provides common functions related to integers."""
import math


class Divisors(object):
    """Allows iteration through proper divisors of n"""
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        limit = math.sqrt(self.n)
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


def is_odd(n):
    """Check if integer n is odd."""
    return (n % 2) != 0


def is_even(n):
    """Check if integer n is even."""
    return (n % 2) == 0


def is_square(n):
    """Check if integer n is a perfect square."""
    x = math.sqrt(n)
    return x == math.floor(x)

