#!/usr/bin/env python
"""P3: Largest prime factor of 600851475143"""

from math import sqrt
from primes import is_prime

N = 600851475143
prime_factors = set()


def main():
    """Find the largest prime factor of N."""
    factors = find_factors(N)

    for factor in factors:
        if is_prime(factor):
            prime_factors.add(factor)

    return sorted(prime_factors)[-1]


def find_factors(n):
    """Find factors of integer n."""
    factors = set()
    counter_factors = set()

    limit = int(sqrt(n))

    for i in range(2, limit):
        if (n % i) == 0:
            factors.add(i)

    for factor in factors:
        counter_factors.add(int(n / factor))

    return factors | counter_factors


if __name__ == '__main__':
    print(("\nLargest prime factor is {}".format(main())))

