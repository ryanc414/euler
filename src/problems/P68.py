#!/usr/bin/env python3

from itertools import permutations, chain

N = 5 
TARGET_LEN = 16



class NGon(object):
    """Represents a 'magic' NGon - a collection of overlapping triplets of
    numbers that all sum to the same total. An Ngon can be uniquely
    specified by n pairs of non-repeating numbers."""
    def __init__(self, values):
        self.n = len(values) 
        self._values = tuple(values)
        self._str = self.gen_str()

    def __str__(self):
        """Return the NGon string."""
        return self._str

    def __hash__(self):
        """Hash on the NGon string."""
        return hash(str(self))

    def __getitem__(self, key):
        """Access NGon values."""
        return self._values[key]

    def gen_str(self):
        """Return a string representation of the Ngon."""
        min_edge_val = self[0][0]
        start_ix = 0

        for i in range(1, self.n):
            next_edge_val = self[i][0]
            if next_edge_val < min_edge_val:
                min_edge_val = next_edge_val
                start_ix = i

        return ''.join(str(x) for x in chain.from_iterable(
            self[(i + start_ix) % self.n] for i in range(self.n)))


def main():
    """Find all possible NGon solutions. Print the solution with the greatest
    numerical value of ngon digits with the required length."""
    ngon_sols = find_all_ngon_sols()
    ngon_strs = set(str(ngon) for ngon in ngon_sols)
    ngon_ints = (int(ngon_str) for ngon_str in ngon_strs
                 if len(ngon_str) == TARGET_LEN) 

    print("Max ngon integer is {}".format(max(ngon_ints)))


def find_all_ngon_sols():
    """Finds all valid NGon solutions. Returns a set to remove solutions
    that are cyclically equivalent (i.e. have the same Ngon strings.)"""
    ngon = [None for _ in range(N)] 
    ngon_set = set()
    numbers = set(range(1, (2 * N) + 1))

    for triplet in permutations(numbers, 3):
        ngon[0] = tuple(triplet)
        total = sum(triplet)
        next_ngon_set = set()
        fill_ngon(ngon, numbers - set(triplet), 1, next_ngon_set, total)
        ngon_set |= next_ngon_set

    return ngon_set


def fill_ngon(ngon, numbers, i, ngon_set, total):
    """Recurisvely find all valid ngon solutions, adding them to ngon_set."""
    assert i < N
    assert len(ngon) == N

    if len(numbers) > 2:
        for pair in permutations(numbers, 2):
            next_triplet = (pair[0], ngon[i - 1][2], pair[1])
            if sum(next_triplet) == total:
                ngon[i] = next_triplet
                fill_ngon(ngon, numbers - set(pair), i + 1, ngon_set, total)
                ngon[i] = None
    else:
        assert len(numbers) == 1
        next_triplet = ((numbers.pop()), ngon[i - 1][2], ngon[0][1])
        if sum(next_triplet) == total:
            ngon[i] = next_triplet
            
            # Sanity check that we have a valid solution
            assert i == N - 1
            assert len(ngon) == N 
            assert all(sum(ngon[i]) == total for i in range(N))
            ngon_set.add(NGon(ngon))


if __name__ == '__main__':
    main()

