#!/usr/bin/env
"""Generate primes using a prime sieve."""
from sys import argv
from math import sqrt


def prime_sieve(n):
    """Find all primes from 2 to n."""
    prime_bool = {num: True for num in range(2, n)}
    
    for i in range(2, int(sqrt(n) + 1)):
        if prime_bool[i]:
            for j in range(i * i, n + 1, i):
                prime_bool[j] = False

    return set(num for (num, prime) in prime_bool.items() if prime)


def is_prime(n):
    """Check if n is prime."""
    # Sanity checking
    assert isinstance(n, int), (
        "Error: cannot check {0} (type {1}) for prime-ness.".format(n, type(n)))
    if n < 2:
        return False

    # Search for possible factors <= sqrt(n)
    limit = int(sqrt(n))

    for i in range(2, limit + 1):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    if len(argv) > 1:
        print(prime_sieve(int(argv[1])))
    else:
        raise Exception("Specify upper limit on commandline.")

