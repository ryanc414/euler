#!/usr/bin/env python3
"""Problem 72: Counting fractions."""

from primes import prime_factors_iter
from itertools import combinations

D_LIMIT = int(1e6)


def count_fractions(d_limit):
    """Count the number of reduced proper fractions for d <= D_LIMIT."""
    return int(sum(totient_sieve(d_limit)))


def totient_sieve(limit):
    """Calculate Euler's totient function for values of n from 1 to n_limit
    inclusive.
    """
    # Start with an array of all possible values of n, such that sieve[i] = i
    # initially.
    sieve = list(range(limit + 1))

    # Iterate through the sieve array. Start from 2 as 1 is not prime.
    for i in range(2, limit + 1):
        # Check if the next value is prime - indicated by its value being equal
        # to its index.
        if sieve[i] == i:
            # Iterate through all multiples of this prime. Multiply their
            # sieve value by (i - 1) / i to account for a term in the totient
            # product.
            for j in range(i, limit + 1, i):
                sieve[j] *= ((i - 1) / i)

    return sieve[2:]


if __name__ == '__main__':
    print(count_fractions(D_LIMIT))

