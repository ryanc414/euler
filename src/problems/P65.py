#!/usr/bin/env python
"""P65 - Find the sum of the digits in the numerator of the 100th continued
fraction approximation of e.

e is given by the continued fraction
e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...]"""

from continued_fractions import ContinuedFraction as CF


def fill_a(n):
    """Fill a_0 to a_n of the coefficients required for the continued fraction
    approximation to e."""
    a = [2]

    for i in range(n):
        if i % 3 == 1:
            a.append(2 * (i // 3 + 1))
        else:
            a.append(1)

    return a


def find_numerator(a, n):
    """Returns the numerator of the nth continued fraction using coefficients
    in a."""
    cf = CF(a)
    cf.find_partial_fracs(n)
    return cf.p[-1]


def main():
    """Find the sum of the 100th continued fraction numerator in the expansion
    of e. Note we start from n = 0 so we actually look for the n = 99 term."""
    n = 99

    a = fill_a(n)

    print("{}th approx to e's digit sum = {}".format(
        n + 1, sum(int(d) for d in str(find_numerator(a, n)))))


if __name__ == '__main__':
    main()

