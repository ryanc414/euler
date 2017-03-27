#!/usr/bin/env python
"""
Digit Cancelling Fractions

A digit-cancelling fraction is defined as a / b = c / d where a, b share a
common digit which is removed to generate c, d. Restricting a, b to be 2 digits
in length and a < b and disregarding trivial examples where a, b are products
of 10 leaves just four such fractions.
"""
from P30 import digits
from P32 import generate_integers
from decimal import Decimal
from operator import mul
from functools import reduce

LENGTH = 2


def main():
    """
    Find the product of all cancelling fractions and factorise it to lowest
    common terms.
    """
    product_fraction = reduce(
        mul, find_all_cancelling_fractions()
    )
    product_fraction.factorise()
    return product_fraction


def find_all_cancelling_fractions():
    """Returns a set of all cancelling fractions."""
    fractions = set()
    number_range = generate_integers(length=LENGTH)
    for x in number_range:
        for y in range(x + 1, max(number_range) + 1):
            if x != y and x % 10 != 0 and y % 10 != 0:
                cancelling_fraction = check_for_cancelled_fraction(x, y)
                if cancelling_fraction is not None:
                    print(cancelling_fraction)
                    fractions.add(cancelling_fraction)
    return fractions


def check_for_cancelled_fraction(x, y):
    """
    Check if shared digits can be cancelled and if so, if cancelling
    results in an equivalent fraction. If the fraction is cancelling then
    it is returned.
    """
    digit = shares_digit(x, y)
    if digit is not None:
        test_fraction = Fraction(x, y)
        cancelled_fraction = cancel_and_divide(x, y, digit)
        if cancelled_fraction is not None:
            if test_fraction == cancelled_fraction:
                return test_fraction


def shares_digit(x, y):
    """Return the first digit shared by numbers x, y."""
    for digit in digits(x):
        if digit in digits(y):
            return digit


def cancel_and_divide(x, y, digit):
    """Cancel a shared digit from x, y then return the fraction x / y."""
    def cancel(n):
        n = str(n).replace(str(digit), '')
        if n == '':
            return None
        return Decimal(n)

    x = cancel(x)
    y = cancel(y)
    if x is not None and y is not None:
        if y != 0:
            return Fraction(x, y)
    return None


class Fraction(object):
    """Represents a fraction x / y."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def factorise(self):
        """Reduce both x, y to lowest common terms."""
        i = self.x
        while i >= 2:
            if self.x % i == 0 and self.y % i == 0:
                self.x /= i
                self.y /= i
            else:
                i -= 1

    def __eq__(self, other):
        """Check for fraction equality."""
        return Decimal(self.x) / Decimal(self.y) == (
            Decimal(other.x) / Decimal(other.y)
        )

    def __mul__(self, other):
        """Multiply two fractions."""
        return Fraction(self.x * other.x, self.y * other.y)

    def __str__(self):
        return "{0} / {1}".format(self.x, self.y)

if __name__ == '__main__':
    print(main())
