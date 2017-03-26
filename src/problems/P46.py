#!/usr/bin/env python
#!/usr/bin/python

from tools.primes import prime_sieve

LIMIT = 10000
PRIMES = prime_sieve(LIMIT)


def main():
    candidates = (n for n in xrange(3, LIMIT, 2) if not PRIMES[n])

    for num in candidates:
        if not prime_and_two_sq(num):
            return num


def prime_and_two_sq(n):
    for i in range(1, LIMIT):
        resid = n - 2 * i * i
        if resid <= 0:
            return False
        if PRIMES[resid]:
            return True




if __name__ == '__main__':
    result = main()
    if result is not None:
        print "{0} violates the conjecture.".format(main())
    else:
        print "Couldn't find any violations. Increase LIMI?"

