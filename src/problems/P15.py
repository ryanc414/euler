#!/usr/bin/env python
"""
Lattice paths
"""
import math


def n_choose_k(n, k):
    """
    Returns binomial coefficients using formula:
    nCk = n! / (k!(n-k)!)
    """
    result = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
    return int(result)


def enumerate_paths(n):
    """
    The number of paths we can choose can be computed from 2nCn
    """
    return n_choose_k(2*n, n)


if __name__ == '__main__':
    grid_size = 20
    print(enumerate_paths(grid_size))
