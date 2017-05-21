#!/usr/bin/env python3
"""P57 - how many fractions in first 1000 expansions of sqrt(2) contain more
digits in numerator than denominator.

Expansion: sqrt(2) = 1 + 1 / (2 + 1 / (2 + ...))"""

from fractions import Fraction

LIMIT = 1000


def main():
    """Use the previous expansion to calculate the next each time."""
    count = 0
    expansion = 0

    for i in range(LIMIT):
        expansion = Fraction(1, 2 + expansion) 
        if numerator_has_more_digits(1 + expansion):
            count += 1
    
    return count


def numerator_has_more_digits(frac):
    return len(str(frac.numerator)) > len(str(frac.denominator))


if __name__ == '__main__':
    print(main())

