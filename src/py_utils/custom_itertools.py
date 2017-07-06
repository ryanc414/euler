#!/usr/bin/env python3
"""Custom extensions to built-in itertools"""

import itertools


def iter_pairs(l):
    """Iterate through all unique pairings of iterable l. The order of each
    pair does not matter (i.e. (1, 2) is equivalent to (2, 1) and the order
    of each pair in the overall pairing does not matter (i.e. [(1, 2), (3, 4)]
    is equivalent to [(3, 4), (1, 2)]."""
    num_el = len(l)
    assert num_el % 2 == 0

    if num_el < 2:
        yield l
        return

    for i in range(1, num_el):
        pair = (l[0], l[i])
        for rest in iter_pairs(l[1:i] + l[i + 1:]):
            yield [pair] + rest

def iter_ordered_pairs(l):
    """Iterate through all possible full pairings of elements in l.
    The order of each pairing matters (i.e. (1, 2) different from (2, 1)
    but the order of the pairs in each pairing does not (i.e. [(1, 2), (3, 4)]
    is equivalent to [(3, 4), (1, 2)]."""
    def iter_pairing(pairs):
        """Iterate through all pairings and generate all possible swaps of the
        unordered pairs."""
        num_pairs = len(pairs)
        for i in range(num_pairs + 1):
            for indices in itertools.combinations(range(num_pairs), i):
                yield swap_pairs(pairs, indices)

    def swap_pairs(pairs, indices):
        """Swap pairs of elements at given indices."""
        new_pairs = pairs

        for ix in indices:
            new_pairs[ix] = pairs[ix][::-1]

        return new_pairs

    for pairing in iter_pairs(l):
        for ordered_pairing in iter_pairing(pairing):
            yield ordered_pairing


if __name__ == '__main__':
    for pairing in iter_ordered_pairs(list(range(6))):
        print(pairing)

