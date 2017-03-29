#!/usr/bin/env python
"""
Power digit sum
"""


def exponent(x):
    return 2 ** x


def sum_digits(n):
    """
    Sums all digits in an integer
    """
    sum = 0
    for digit in str(n):
        sum += int(digit)

    return sum


if __name__ == '__main__':
    n = 1000
    print(sum_digits(exponent(n)))
