#!/usr/bin/env python3

import primes
import itertools
import functools
from math import sqrt
from decimal import Decimal, getcontext
from operator import mul

LIMIT = int(1e7)


class PE70(object):
    """Find minimal value of n/phi(n) for which phi(n) is a permutation of
    n. phi(n) = n * product(1 - 1/p) for p prime factors of n. Therefore
    n/phi(n) = 1 for prime n."""
    def __init__(self, limit, p_limit):
        self.primes = sorted(primes.prime_sieve(int(p_limit)))
        self.num_primes = len(self.primes)
        self.find_n(limit)

    def find_n(self, limit):
        """Find the value of n that gives a minimal ratio n/phi(n).
        Generate n from pairs of prime factors."""
        min_ratio = None

        for p in self.primes:
            for q in self.primes:
                n = p * q
                if n > limit:
                    continue

                phi = self.phi(p, q)
                ratio = n / phi

                if self.is_perm(n, phi) and (
                        (min_ratio is None) or (ratio < min_ratio)):
                    min_ratio = ratio
                    min_ratio_n = n

        return min_ratio_n

    def phi(self, p, q):
        """Calculate phi(n). For n = p * q with prime factors p and q,
        phi(n) = (p - 1)(q - 1)."""
        return (p - 1) * (q - 1)

    def is_perm(self, x, y):
        return (x != y) and sorted(str(x)) == sorted(str(y))


def main():
    pe70 = PE70(LIMIT, 5000)
    n = pe70.find_n(LIMIT)
    print("n = {0} gives minimal phi(n)/n.".format(n))


if __name__ == '__main__':
    main()

