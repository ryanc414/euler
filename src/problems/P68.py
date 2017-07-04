#!/usr/bin/env python3
"""P68 - Magic N-gons"""

from itertools import permutations, chain
from collections import deque

N = 5


class NGon(object):
    def __init__(self, n, values):
        self.n = n
        self.values = [[None, None, None] for _ in range(n)]
        self.fill_values(deque(values))

    def verify(self):
        """Verify that the values form a self-consistent solution"""
        total = sum(self.values[0])

        for i in range(1, self.n):
            if self.values[i][0] <= self.values[0][0]:
                return False
            if sum(self.values[i]) != total:
                return False

        return True

    def __str__(self):
        return str(self.values)

    def fill_values(self, values):
        for i in range(N):
            for j in range(2):
                self.values[i][j] = values.popleft()
            self.values[i - 1][2] = self.values[i][1]


def main():
    ngon_list = []
    ngon_int_list = []

    for value_set in permutations(range(1, (2 * N) + 1)):
        ngon = NGon(N, value_set)
        if ngon.verify():
            ngon_list.append(ngon)

    for ngon in ngon_list:
        ngon_str = concat_to_str(ngon)
        if len(ngon_str) == 16:
            ngon_int_list.append(int(ngon_str))

    print("Max ngon integer is {}".format(max(ngon_int_list)))


def concat_to_str(ngon):
    return ''.join(str(x) for x in chain.from_iterable(ngon.values))



if __name__ == '__main__':
    main()

