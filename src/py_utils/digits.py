#!/usr/bin/env python
"""Provides functions for working with digits in integers."""


def sum_digits(n):
    """
    Sums all digits in an integer
    """
    sum = 0
    for digit in str(n):
        sum += int(digit)

    return sum

