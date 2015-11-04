#!/usr/bin/env
"""Generate primes using a prime sieve."""
from sys import argv


def prime_sieve(n):
    """Find all primes from 2 to n."""
    def discard_multiples(prime):
        i = 2
        multiple = i * prime
        while multiple < n:
            primes[multiple] = False
            i += 1
            multiple = i * prime

    def find_next_prime(prime):
        prime += 1
        while prime < n:
            if primes[prime]:
                return prime
            else:
                prime += 1

    primes = {num: True for num in range(2, n)}
    p = 2

    while True:
        discard_multiples(p)
        p = find_next_prime(p)
        if p is None:
            break

    return primes

if __name__ == '__main__':
    if len(argv) > 1:
        print prime_sieve(int(argv[1]))
    else:
        raise Exception("Specify upper limit on commandline.")

