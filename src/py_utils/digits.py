#!/usr/bin/env python
"""Provides functions for working with digits in integers."""


def sum_digits(n):
    """
    Sums all digits in an integer
    """
    sum = 0
    for digit in gen_reverse_digits(n):
        sum += digit

    return sum


def gen_reverse_digits(n):
    """Efficiently generate digits of an integer in reverse order."""
    if n == 0:
        yield n

    while n:
        yield n % 10
        n //= 10

