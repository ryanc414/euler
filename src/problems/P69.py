#!/usr/bin/env python
from math import sqrt
from primes import prime_sieve

LIMIT = 1000000


class PE69(object):
    """Find the number n less than limit, for which n/phi(n) is maximal.
    phi(n) is Euler's totient function which gives the number of integers
    less than n which are coprime to n."""
    def __init__(self, limit):
        self.primes = sorted(prime_sieve(limit))
        (self.max_val, self.max_n) = self.find_max_val()

    def n_over_phi(self, n):
        """Euler's product formula gives phi(n) = n * product(1 - 1/p)
        for prime factors p of n. Therefore n/phi(n) is
        1 / product(1 - 1/p)."""
        product = 1
        limit = int(sqrt(n))
        for p in self.primes:
            if p > limit:
                break
            if n % p == 0:
                product *= (1 - 1 / p)

        return 1 / product

    def find_max_val(self):
        """Find the value of n less than the limit that gives the maximal
        value for n/phi(n)."""
        max_val = 0
        max_n = None

        for n in range(1, LIMIT):
            val = self.n_over_phi(n)
            if val > max_val:
                max_val = val
                max_n = n

        return (max_val, max_n)


if __name__ == '__main__':
    pe69 = PE69(LIMIT)
    print("Maximum n/phi(n) = {0} for n = {1}".format(pe69.max_val, pe69.max_n))

