#!/usr/bin/env python3
"""P68 - Magic N-gons"""

from itertools import permutations, chain
from custom_itertools import iter_ordered_pairs

N = 5
MUST_BE_IN_EDGE = 10

class NGon(object):
    """Represents a 'magic' NGon - a collection of overlapping triplets of
    numbers that all sum to the same total. An Ngon can be uniquely
    specified by n pairs of non-repeating numbers."""
    def __init__(self, n, values):
        self.n = n
        self.values = [[None, None, None] for _ in range(n)]
        self.fill_values(values)

    def __str__(self):
        return ''.join(str(x) for x in chain.from_iterable(self.values))

    def verify(self):
        """Verify that the values form a self-consistent solution"""
        total = sum(self.values[0])

        for i in range(1, self.n):
            if self.values[i][0] <= self.values[0][0]:
                return False
            if sum(self.values[i]) != total:
                return False

        return True

    def fill_values(self, values):
        """Take an input list of value pairs and generate a magic Ngon,
        filling the overlapping values in each triplet."""
        # First rotate the values list until we have the lowest edge value at
        # the start.
        min_edge_val = (2 * self.n) + 1
        for i in range(self.n):
            if values[i][0] < min_edge_val:
                min_edge_val = values[i][0]
                min_edge_ix = i

        values = values[min_edge_ix:] + values[:min_edge_ix]

        # Now fill in the overlapping third element of each triplet
        for i in range(self.n):
            for j in range(2):
                self.values[i][j] = values[i][j]
            self.values[i - 1][2] = self.values[i][1]


def main():
    """Generate all possible Ngon solutions. Of those that verify as correct,
    convert to strings of digits. Print the numerically largest such digit
    string."""
    ngon_list = []
    ngon_int_list = []

    for value_set in iter_values(range(1, (2 * N) + 1)):
        ngon = NGon(N, value_set)
        if ngon.verify():
            ngon_list.append(ngon)

    for ngon in ngon_list:
        ngon_str = str(ngon)
        assert len(ngon_str) == 16
        ngon_int_list.append(int(ngon_str))

    print("Max ngon integer is {}".format(max(ngon_int_list)))


def iter_values(vals):
    """Iterates through all possible unique orderings of pairings for a list
    of values. Ignores orderings that are cyclically equivalent."""
    num_pairs = len(vals) // 2

    for pairing in iter_ordered_pairs(list(vals)):
        for p in permutations(pairing[1:]):
            value_list = [pairing[0]] + list(p)

            # Optimization: only yield value lists if 10 is the first value
            # in a pairing, as only these will give 16-digit strings.
            for i in range(num_pairs):
                if value_list[i][0] == MUST_BE_IN_EDGE:
                    yield value_list
                    break


if __name__ == '__main__':
    main()

