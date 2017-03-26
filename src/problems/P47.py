#!/usr/bin/python

from math import sqrt

NUM_FACTORS = 4 

def main():
    count = 0
    n = 2 

    while count != NUM_FACTORS:
        factors = distinct_prime_factors(n)
        if len(factors) != NUM_FACTORS:
            count = 0;
        else:
            count = count + 1
        n = n + 1

    return (n - NUM_FACTORS)


def distinct_prime_factors(n):
    limit = int(sqrt(n))
    prime = True
    factors = set()

    for i in xrange(2, limit + 1):
        if n % i == 0:
            prime = False
            factors.update(distinct_prime_factors(i))
            factors.update(distinct_prime_factors(n / i))

    if prime:
        factors.add(n)

    return factors

if __name__ == '__main__':
    print "First number is {0}".format(main())

