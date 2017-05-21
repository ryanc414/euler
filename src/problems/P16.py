#!/usr/bin/env python
"""
Power digit sum
"""
from digits import sum_digits


def exponent(x):
    return 2 ** x


if __name__ == '__main__':
    n = 1000
    print(sum_digits(exponent(n)))

