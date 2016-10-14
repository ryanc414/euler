#!/usr/bin/python

from primes import prime_sieve

LIMIT = 1000000

def main():
    # generate all primes below limit
    primes = prime_sieve(LIMIT)

    # start with a set of all odd non-primes below LIMIT
    candidates = set(n for n in range(LIMIT) if n not in primes and n % 2 == 1 and n != 1)

    # now, remove each number that can be written as a prime plus 2 * a square
    for num in prime_plus_two_sq(primes):
        candidates.discard(num)

    # finally, print smallest remaining candidate
    if len(candidates) > 0:
        return min(candidates)


def prime_plus_two_sq(primes):
    for prime in primes:
        for i in xrange(LIMIT):
            result = prime + 2 * i * i
            if result > LIMIT:
                break
            else:
                yield result





if __name__ == '__main__':
    result = main()
    if result is not None:
        print "{0} violates the conjecture.".format(main())
    else:
        print "Couldn't find any violations. Increase LIMI?"

