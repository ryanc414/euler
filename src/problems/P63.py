#!/usr/bin/env python3
"""P63 - Powerful Digit Counts."""
import itertools


def main():
    """Sum the total count of powerful digits."""
    print("Sum: {}".format(sum(find_all_powerful_ints())))


def find_all_powerful_ints():
    """Count the number of n-digit integers x such that x = y^n for some
    integers y and n."""
    for i in itertools.count(start=1):
        next_count = count_powerful_ints(i)
        if next_count:
            yield next_count
        else:
            break


def count_powerful_ints(n_digits):
    """Count the number of n-digit integers x such that x = y^n for some
    integer y, with given n."""
    lower_limit = 10 ** (n_digits - 1)
    return sum(1 for y in range(1, 10) if y ** n_digits >= lower_limit)


if __name__ == '__main__':
    main()

