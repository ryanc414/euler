#!/usr/bin/env python


OTHER_PRIMES = [3, 7, 109, 673]

from tools.primes import prime_sieve, is_prime


def main():
    n = 675

    while (not concat_with(n)):
        print n
        n += 2

    print sum(OTHER_PRIMES) + n


def concat_with(n):
    if not is_prime(n):
        return False

    for p in OTHER_PRIMES:
        if not is_prime(int(str(n) + str(p))):
            return False
        if not is_prime(int(str(p) + str(n))):
            return False

    return True


if __name__ == '__main__':
    main()
