#!/usr/bin/env python3

from math import sqrt, floor
from itertools import count
from continued_fractions import ContinuedFractionSqRoot as CFSqrt

N = 10000


def is_odd(n):
    """Returns True if integer n is odd."""
    return bool(n % 2)

if __name__ == '__main__':
    print(sum(1 for i in range(1, N + 1)
              if is_odd(CFSqrt(i).find_period())))

