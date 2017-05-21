#!/usr/bin/env python3
"""Distinct Powers"""
LOWER_LIMIT = 2
UPPER_LIMIT = 100


def main():
    """
    Find the number of distinct powers a^b for:
    LOWER_LIMIT <= (a, b) <= UPPER_LIMIT.
    """
    return len(distinct_powers())


def distinct_powers():
    """Add all unique powers a^b to set."""
    power_set = set()
    for a in range(LOWER_LIMIT, UPPER_LIMIT + 1):
        for b in range(LOWER_LIMIT, UPPER_LIMIT + 1):
            power_set.add(a ** b)
    return power_set


if __name__ == '__main__':
    print(main())
