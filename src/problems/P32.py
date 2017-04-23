#!/usr/bin/env python
"""
Pandigital Products

A product z is pandigital iff the statement "x * y = z" contains all of
the digits 1 to n once only for valid multiplicand/multiplier pair x, y.
"""
DIGITS = list(range(1, 10))
STR_DIGITS = list(map(str, DIGITS))


def main():
    """Sum all unique pandigital products."""
    return sum(unique_pandigital_products())


def unique_pandigital_products():
    """
    This function checks pairs of digits with lengths supplied by digit_pairs()
    to see if their product identity is pandigital - if so it is added to the
    set (this automatically takes care of possible double-counting).
    """
    products = set()
    for pair in digit_pairs():
        for x in generate_integers(length=pair[0]):
            for y in generate_integers(length=pair[1]):
                product = x * y
                if is_pandigital(x, y, product):
                    products.add(product)
    return products


def digit_pairs():
    """
    The product of numbers of length i, j will be length i + j - 1 or i + j.
    Therefore, digit pairs of length i, j are worth considering if 2(i + j) =
    9 or 10.
    """
    good_pairs = set()
    num_digits = len(DIGITS)
    target_sums = (num_digits, num_digits + 1)
    for i in range(num_digits):
        for j in range(i, num_digits):
            digit_sum = 2 * (i + j)
            if digit_sum in target_sums:
                good_pairs.add((i, j))
            elif digit_sum > target_sums[1]:
                break
    return good_pairs


def generate_integers(length=1):
    """Generates all integers of a given length."""
    upper_limit = 10 ** length
    lower_limit = upper_limit // 10
    return range(lower_limit, upper_limit)


def is_pandigital(x, y, product):
    """Check if the identity "x * y = product" is pandigital."""
    all_digits = sorted(str(x) + str(y) + str(product))
    if all_digits == STR_DIGITS:
        return True
    return False


if __name__ == '__main__':
    print("Sum of pandigital products is {0}".format(main()))

