#!/usr/bin/env python
"""Digit Fifth Powers"""
from math import log10
from digits import gen_reverse_digits

LOWER_LIMIT = 2  # Exclude trivial 1^5 = 1
POWER = 5  # we are interested in fifth powers


def find_upper_limit():
    """
    Find the upper limit for numbers that could be written as the sum of their
    digit powers. Each digit can contribute a maximum of 9^POWER to the sum,
    so any number that exceeds (9^POWER) * number_of_digits will be a valid
    upper limit.
    """
    number_of_digits = 1
    max_digit = 9 ** POWER
    while True:
        num = 10 ** (number_of_digits - 1)
        if number_of_digits * max_digit < num:
            return num
        else:
            number_of_digits += 1


UPPER_LIMIT = find_upper_limit()


def main():
    """
    Find the sum of all numbers between LOWER_LIMIT and UPPER_LIMIT that are
    equal to the sum of their digits each raised to POWER.
    """
    sum_fifth_powers = 0
    for number in range(LOWER_LIMIT, UPPER_LIMIT):
        if sum_of_power_digits(number, POWER) == number:
            sum_fifth_powers += number
    return sum_fifth_powers



def sum_of_power_digits(n, power):
    """
    Sum each digit in an integer raised to power.
    """
    return sum(digit ** power for digit in gen_reverse_digits(n))


if __name__ == '__main__':
    print(main())

