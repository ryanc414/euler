#!/usr/bin/env python3

from math import factorial

LIMIT = 101
TARGET = int(1e6)


def main():
    count = 0

    for n in range(1, LIMIT):
        for r in range(1, n):
            if nCr(n, r) > TARGET:
                count += 1

    return count


def nCr(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))


if __name__ == '__main__':
    print(main())

