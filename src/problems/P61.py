#!/usr/bin/env python
"""P61 - find an ordered set of 6 4-digit numbers that are cyclic (last and
first two digits of neighbouring numbers overlap) and contain one each of
triangle, square, pentagonal, hexagonal, heptagonal and octagonal numbers
in no particular order."""

from collections import deque
from tree import Found


def main():
    lowest_set = find_lowest_set()
    print("Sum of lowest set: {0}".format(sum(lowest_set)))


def triangle(n):
    return n * (n + 1) // 2


def square(n):
    return n * n


def pentagonal(n):
    return n * (3 * n - 1) // 2


def hexagonal(n):
    return n * (2 * n - 1)


def heptagonal(n):
    return n * (5 * n - 3) // 2


def octagonal(n):
    return n * (3 * n - 2)


def iter_series(series_func):
    lower_limit = 1000
    upper_limit = 10000
    n = 1

    while series_func(n) < lower_limit:
        n += 1

    next_p = series_func(n)
    while next_p < upper_limit:
        yield next_p
        n += 1
        next_p = series_func(n)


def find_lowest_set():
    """Find the lowest set that is cyclic and contains one of each series
    type."""
    def find_next_element(curr_elements, remaining_series):
        """Recursively add elements to the list of possibles, either to the
        start or end. Raise a SetFound signal when a complete set is found."""
        for series in remaining_series:
            for n in iter_series(series):
                if is_cyclic(curr_elements[-1], n):
                    curr_elements.append(n)
                    remaining_series.remove(series)
                    if len(remaining_series) > 0:
                        find_next_element(curr_elements, remaining_series)
                    elif is_cyclic(curr_elements[-1], curr_elements[0]):
                        raise Found()

                    # If we get here, it means that no valid sets were found.
                    # Reset and continue looking at this level.
                    curr_elements.pop()
                    remaining_series.add(series)

                if is_cyclic(n, curr_elements[0]):
                    curr_elements.appendleft(n)
                    remaining_series.remove(series)
                    if len(remaining_series) > 0:
                        find_next_element(curr_elements, remaining_series)
                    elif is_cyclic(curr_elements[-1], curr_elements[0]):
                        raise Found()

                    # If we get here, it means that no valid sets were found.
                    # Reset and continue looking at this level.
                    curr_elements.popleft()
                    remaining_series.add(series)

    test_series = set((square, pentagonal, hexagonal, heptagonal, octagonal))

    try:
        for n in iter_series(triangle):
            cyclic_set = deque([n])
            find_next_element(cyclic_set, test_series)
    except Found:
        return cyclic_set
    else:
        raise Exception("No valid set found.")


def is_cyclic(a, b):
    """Check if the last two digits of a are the same as the first two of b."""
    return str(a)[-2:] == str(b)[:2]


if __name__ == '__main__':
    main()

