#!/usr/bin/env python
"""P5: Smallest integer divisible by all integers in range 1-20"""

from itertools import count

LIMIT = 20


def main():
    for n in count(LIMIT, LIMIT):
        for i in range(3, LIMIT):
            if n % i != 0:
                break
        else:
            return n


if __name__ == '__main__':
    print("Smallest integer divisible by all integers 1-20: {}".format(main()))

