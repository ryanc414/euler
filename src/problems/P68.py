#!/usr/bin/env python3
"""P68 - Magic N-gons"""

from itertools import permutations, chain
from custom_itertools import iter_ordered_pairs

N = 5


class NGon(object):
    def __init__(self, n, values):
        self.n = n
        self.values = [[None, None, None] for _ in range(n)]
        self.fill_values(values)

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
        # First rotate the values list until we have the lowest edge value at
        # the start.
        min_edge_val = (2 * self.n) + 1
        for i in range(self.n):
            if values[i][0] < min_edge_val:
                min_edge_val = values[i][0]
                min_edge_ix = i

        values = values[min_edge_ix:] + values[:min_edge_ix]

        for i in range(self.n):
            for j in range(2):
                self.values[i][j] = values[i][j]
            self.values[i - 1][2] = self.values[i][1]


def main():
    ngon_list = []
    ngon_int_list = []

    for value_set in iter_values(range(1, (2 * N) + 1)):
        ngon = NGon(N, value_set)
        if ngon.verify():
            ngon_list.append(ngon)

    for ngon in ngon_list:
        ngon_str = concat_to_str(ngon)
        if len(ngon_str) == 16:
            ngon_int_list.append(int(ngon_str))

    print("Max ngon integer is {}".format(max(ngon_int_list)))


def iter_values(vals):
    num_pairs = len(vals) // 2

    for pairing in iter_ordered_pairs(list(vals)):
        for p in permutations(pairing[1:]):
            yield [pairing[0]] + list(p)


def concat_to_str(ngon):
    return ''.join(str(x) for x in chain.from_iterable(ngon.values))



if __name__ == '__main__':
    main()

