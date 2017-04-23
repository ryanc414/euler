#!/usr/bin/env python
"""
Digit Factorials

Finds the sum of all n equal to the sum of the factorial of their digits,
for n > 9.
"""
from math import factorial
from P30 import digits

DIGITS = list(range(10))


def find_digit_factorials():
    """
    Cache factorials of DIGITS so that we don't have to repeatedly calculate
    them.
    """
    return {digit: factorial(digit) for digit in DIGITS}


FACT_DIGITS = find_digit_factorials()


def find_upper_limit():
    """
    When max_digit! * num_digits < 10 ** (num_digits - 1) we can stop looking
    for curious factorials.
    """
    num_digits = 1
    max_digit = FACT_DIGITS[max(DIGITS)]
    while True:
        min_num = 10 ** (num_digits - 1)
        if num_digits * max_digit < min_num:
            return min_num
        else:
            num_digits += 1


# Ignore trivial cases 1! = 1 and 2! = 2 by starting from double-digits.
LOWER_LIMIT = 10
UPPER_LIMIT = find_upper_limit()


def main():
    """Sum all curious factorials between LOWER_LIMIT and UPPER_LIMIT."""
    sum_digit_factorials = 0
    for i in range(LOWER_LIMIT, UPPER_LIMIT):
        digit_factorial_sum = find_digit_factorial_sum(i)
        if digit_factorial_sum == i:
            sum_digit_factorials += i
    return sum_digit_factorials


def find_digit_factorial_sum(n):
    """Sum the factorials of digits in an integer n."""
    return sum(FACT_DIGITS[digit] for digit in digits(n))


if __name__ == '__main__':
    print("Sum of digit factorials is {0}".format(main()))

