#!/usr/bin/env python
"""
Longest Collatz sequence
"""


class CollatzSequence(object):
    """
    A Collatz sequence is defined iteratively as:
    n -> n/2 (n is even)
    n -> 3n + 1 (n is odd)
    It terminates when n is 1.
    """
    def __init__(self, n_initial):
        self.n = n_initial

    def __iter__(self):
        """
        Define a Collatz sequence.
        """
        while self.n != 1:
            if self.n % 2 == 0:  # check if n is even
                self.n /= 2
            else:  # n is odd
                self.n = 3 * self.n + 1
            yield self.n
        yield self.n  # make sure we yield the final term (1)

    def __len__(self):
        """
        Find length of a Collatz sequence starting with i
        :return int: length of sequence
        """
        if self.n == 1:
            return 1
        length = 1
        for term in self:
            length += 1
        return length


def find_starter_lengths(n):
    """
    Find the longest Collatz sequence that starts with an integer
    less than n.
    :return int, int: starting number
    """
    starter_lengths = {1: 1}

    # we're not interested in the trivial sequence starting with 1
    # so start from 2 instead.
    for i in range(2, n):
        term_number = 1
        for term in CollatzSequence(i):
            if term in starter_lengths:
                starter_lengths[i] = starter_lengths[term] + term_number
                break
            term_number += 1
        else:  # no break
            starter_lengths[i] = term_number

    return starter_lengths


def find_max_starter(starters_dict):
    """
    Find the starter key corresponding to the maximum sequence length
    :param starters_dict: dictionary of starters: lengths
    :return: maximal starter
    """
    values = list(starters_dict.values())
    keys = list(starters_dict.keys())
    return keys[values.index(max(values))]


if __name__ == '__main__':
    N = int(1e6)  # we are interested in terms below 1 million
    starter = find_max_starter(find_starter_lengths(N))
    print("Longest starter was {0}".format(starter))
