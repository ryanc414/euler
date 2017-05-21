#!/usr/bin/env python3
"""Non-abundant sums"""
from num_funcs import sum_of_divisors

UPPER_LIMIT = 28123


def main():
    """Prints the sum of all non-abundant sums"""
    print(sum(non_abundant_sums()))


def non_abundant_sums():
    """Returns a set of non-abundant sums."""
    return set(range(1, UPPER_LIMIT+1)) - abundant_sums()


def abundant_sums():
    """Returns all abundant number sums."""
    abundant_number_sums = set()
    abundant_numbers = generate_abundant_numbers()
    total_abundant_numbers = len(abundant_numbers)
    for i in range(total_abundant_numbers):
        for j in range(i, total_abundant_numbers):
            abundant_sum = abundant_numbers[i] + abundant_numbers[j]
            if abundant_sum <= UPPER_LIMIT:
                abundant_number_sums.add(abundant_sum)
    return abundant_number_sums


def generate_abundant_numbers():
    """Returns a list of abundant numbers below upper_limit (inclusive)."""
    return [
        i for i in range(1, UPPER_LIMIT+1) if sum_of_divisors(i) > i]


if __name__ == '__main__':
    main()
