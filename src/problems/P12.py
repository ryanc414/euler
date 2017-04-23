#!/usr/bin/env python
"""
Highly divisible triangle numbers
"""

from itertools import count
from math import sqrt

TARGET_DIVISORS = 500


def find_num_divisors(n):
    """
    Finds the number of divisors of an integer n
    """
    assert n >= 0
    if n <= 1:
        return n
    num_divisors = 1
    i = 2
    count = 0
    limit = int(sqrt(n))

    while True:
        if i > limit:
            if i != n:
                # count previous factor
                num_divisors *= (count + 1)
                count = 0
            count += 1
            num_divisors *= (count + 1)
            break
        elif n % i == 0:  # found a factor
            n /= i
            limit = n ** 0.5
            count += 1
        else:
            # i is not a factor, so increment
            if i == 2:
                i += 1
            else:
                i += 2
            num_divisors *= count + 1
            count = 0

    return num_divisors


def main():
    """
    Finds first triangle number to have more than the target number
    of divisors.
    """
    n = 0

    for i in count(1):
        n += i
        num_divisors = find_num_divisors(n)
        if num_divisors > TARGET_DIVISORS:
            print("First triangle number to have over {3} divisors:"
                  " {0}th number is {1} and has {2} divisors.".format(
                      i, n, num_divisors, TARGET_DIVISORS))
            break


if __name__ == '__main__':
    main()

