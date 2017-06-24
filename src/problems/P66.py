#!/usr/bin/env python
"""P66 - for the Pell equation x^2 - D y^2 = 1, find value of D <= 1000 such
that the minimal solution in x is maximised, with both x and y as positive
integers."""

import math
import itertools
import num_funcs
import continued_fractions as cf

D_MAX = 1000


def find_smallest_x(D):
    """Find the minimal positive integer x that solves the Pell equation. It
    can be shown that solutions can be found from the continued fraction
    approximations to the square root of D - see
    http://mathworld.wolfram.com/PellEquation.html"""
    cfsqrt = cf.ContinuedFractionSqRoot(D)

    if cfsqrt.is_square:
        # No solution for square D. Return 0 to signify this.
        return 0

    r = cfsqrt.period - 1
    if num_funcs.is_odd(r):
        limit = r
    else:
        limit = 2 * r + 1

    cfsqrt.find_partial_fracs(limit)

    # Sanity check that we have found a valid solution
    x = cfsqrt.p[-1]
    y = cfsqrt.q[-1]
    assert(((x ** 2) - (D * (y ** 2))) == 1)

    return x


def main():
    """For D <= D_MAX, find which value of D gives the largest minimal x
    solution in positive integers for the Pell equation."""
    max_x = 0

    for D in range(2, D_MAX + 1):
        new_x = find_smallest_x(D)
        if new_x > max_x:
            max_x = new_x
            max_x_D = D

    print("Largest minimal x produced for D = {}".format(max_x_D))


if __name__ == '__main__':
    main()

