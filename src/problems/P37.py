#!/usr/bin/env python
"""Trucatable Primes"""

from tools.iterable_nums import IterableInt
from tools.primes import prime_sieve

DIGIT_PRIMES = set([2, 3, 5, 7])
UPPER_LIMIT = int(10e5)
PRIMES = prime_sieve(UPPER_LIMIT)
COUNT_LIMIT = 11

def main():
    return sum(truncatable_primes())


def truncatable_primes():
    # ignore single-digit primes by starting from 11
    n = IterableInt(11)
    count = 0
    while count < COUNT_LIMIT:
        # check if both first and last digits are prime
        if n.digits[0] in DIGIT_PRIMES:
            if n.digits[-1] in DIGIT_PRIMES:
                if is_truncatable_prime(n):
                    count += 1
                    print(n)
                    yield n
            n += 1
        else:
            # first digit isn't prime, so increment it by 1
            n += 10 ** (len(n) - 1)


def is_truncatable_prime(n):
    def truncate_and_check(m, increment):
        while m:
            if m not in PRIMES:
                return False
            m = increment(m)
        return True

    def right_to_left(m):
        return m / 10
    
    def left_to_right(m):
        return m - m.digits[0] * (10 ** (len(m) - 1))
        
    return truncate_and_check(n, right_to_left) and truncate_and_check(n, left_to_right)
           

if __name__ == '__main__':
    print("Sum of truncatable primes is {0}".format(main()))

