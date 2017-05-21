#!/usr/bin/env python3
"""Reciprocal cycles"""
from math import log10
from decimal import *

d_MAX = 1000
PREC = 28


def main():
    """Returns longest cycle length of 1/d decimals for d < d_MAX"""
    longest_cycle_length = 0
    for i in range(2, d_MAX):
        current_length = cycle_length(i)
        if current_length > longest_cycle_length:
            d = i
            longest_cycle_length = current_length
    return d


def cycle_length(d):
    """Returns cycle length for decimal 1/d"""
    remainder = 1

    # Check for terminating decimal
    for i in range(d):
        remainder = (remainder * 10) % d

    if remainder == 0:
        return 0

    # We know the decimal doesn't terminate. Store the current remainder
    # and count how many steps it takes to repeat.
    remainder_0 = remainder
    remainder = (remainder * 10) % d
    cycle_len = 1

    while remainder != remainder_0:
        cycle_len += 1
        remainder = (remainder * 10) % d

    return cycle_len


if __name__ == '__main__':
    print(main())

