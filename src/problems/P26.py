#!/usr/bin/env python
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
    length = len(str(Decimal(1) / Decimal(d)))
    if length < PREC:
        return 0

    for p in range(1, d_MAX):
        n = int(10 ** p) - 1 % d
        if n % d == 0:
            return int(log10(n / d)) + 1


if __name__ == '__main__':
    print(main())