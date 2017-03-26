#!/usr/bin/env python
# Nth prime

from tools.primes import is_prime
from itertools import count

N = 10001  # We want to find the 10,001st prime


def main():
    prime_count = 0

    for i in count(1):
        if is_prime(i):
            prime_count += 1
        if prime_count == N:
            break

    print i 

        
if __name__ == '__main__':
    main()

