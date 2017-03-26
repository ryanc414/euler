#!/usr/bin/env python
"""
Print a lit of all Collatz sequence lengths starting at values less than N
"""
import P14


if __name__ == '__main__':
    N = int(1e7)
    starters = P14.find_starter_lengths(N)
    with open('seq.txt', 'w') as f:
        for k, v in starters.iteritems():
            f.write("{0} {1}\n".format(k, v))
