#!/usr/bin/env python3

from primes import prime_sieve
from itertools import combinations

LIMIT = int(1e6)
PRIMES = set(str(prime) for prime in prime_sieve(LIMIT) if prime > 10)
TARGET = 8
DIGITS = [str(n) for n in range(10)]


def main():
    for prime in sorted(PRIMES):
        for indices in choose_digit_indices(prime):
            if size_of_familly(prime, indices) >= TARGET:
                return (prime, indices)


def size_of_familly(prime, indices):
    num_primes = 0
    for digit in DIGITS:
        new_prime = replace_digits(prime, indices, digit)
        if new_prime in PRIMES:
            num_primes += 1
    return num_primes


def replace_digits(prime, indices, digit):
    prime = [c for c in prime]
    for i in indices:
        prime[i] = digit
    return ''.join(prime)


def choose_digit_indices(numstr):
    found_digits = {n: set() for n in DIGITS}

    for digit in DIGITS:
        for i in range(len(numstr)):
            if numstr[i] == digit:
                found_digits[digit].add(i)

    return (c for indices in found_digits.values()
            if len(indices) > 0
            for c in all_combinations(indices))


def all_combinations(elements):
    return (c for i in range(1, len(elements) + 1)
            for c in combinations(elements, i))


if __name__ == '__main__':
    print(main())

