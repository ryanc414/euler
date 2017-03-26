#!/usr/bin/env python
"""Project Euler Problem 60 - Prime Pair Sets"""

from tools.primes import prime_sieve, is_prime

N = 5 
UPPER_LIMIT = int(1e4)


def main():
    """Find the lowest sum of a set of 5 primes for which each pair
    concatenates to form other primes."""
    primes = sorted(prime_sieve(UPPER_LIMIT))

    lowest_set = find_lowest_set(primes)

    print lowest_set
    print "Sum of lowest set: {0}".format(sum(int(p) for p in lowest_set))


class SetFound(Exception):
    """Signal raised when a big enough set is found."""
    pass


def find_lowest_set(primes):
    """Finds a set of 5 primes where each pair concatenates to form another
    prime. Assume that these are rare enough for us to find the one with the
    lowest sum first."""
    def find_next(primes, possible_set, last):
        """Find the next prime to add to the set, recursively. Jump back up
        the stack when we find a big enough set."""
        for p in primes:
            for q in possible_set:
                if p == q or not concats_to_prime(p, q):
                    break
            else:
                possible_set.add(p)
                if len(possible_set) == N:
                    raise SetFound()
                else:
                    find_next(primes, possible_set, p)
        possible_set.remove(last)
 
    possible_set = set()

    try:
        find_next(primes, possible_set, None)
    except SetFound:
        return possible_set 
    else:
        raise Exception("Couldn't find a big enough set.")


def concats_to_prime(p, q):
    """Decide if a pair of primes mutually concatenates to form two different
    primes."""
    return (is_prime(int(str(p) + str(q))) and
            is_prime(int(str(q) + str(p))))


if __name__ == '__main__':
    main()

