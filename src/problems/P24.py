#!/usr/bin/env python
"""Lexicographic permutations"""
from itertools import permutations

N = 9
DIGITS = list(range(N + 1))
TERM = int(1e6)

def main():
    i = 1
    for perm in permutations(DIGITS):
        if i == TERM:
            print(''.join(map(str, perm)))
            break
        else:
            i += 1


if __name__ == '__main__':
    main()
