#!/usr/bin/env python
"""
Circular Primes
"""
from P30 import digits

UPPER_LIMIT = int(1e6)


def main():
    return len(find_circular_primes())


def find_circular_primes():
    circular_primes = set()
    prime_map = prime_sieve(UPPER_LIMIT)
    for num, is_prime in prime_map.iteritems():
        if is_prime:
            for rot in rotations(num):
                if not prime_map[rot]:
                    break
            else:
                circular_primes.add(num)
    return circular_primes


def rotations(n):
    def rotate(digit_list, length):
        rotation = [None for _ in xrange(length)]
        for j in xrange(length):
            if j < length - 1:
                rotation[j + 1] = digit_list[j]
            else:
                rotation[0] = digit_list[j]
        return rotation

    def convert_list_to_int(int_list):
        """Converts a list of integer digits to an integer."""
        j = 0
        ans = 0
        for num in int_list[::-1]:
            ans += num * (10 ** j)
            j += 1
        return ans

    n_digits = list(digits(n))[::-1]
    limit = len(n_digits)
    for i in xrange(limit):
        n_digits = rotate(n_digits, limit)
        yield convert_list_to_int(n_digits)


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
        while prime <= n:
            if primes[prime]:
                return prime
            else:
                prime += 1

    primes = {num: True for num in range(2, n + 1)}
    p = 2

    while True:
        discard_multiples(p)
        p = find_next_prime(p)
        if p is None:
            break

    return primes


if __name__ == '__main__':
    print main()
