#!/usr/bin/env python
"""Sum of amicable numbers less than 10000"""
from math import sqrt
N = 10000


class Divisors(object):
    """Allows iteration through proper divisors of n"""
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        limit = sqrt(self.n)
        for i in range(1, int(limit) + 1):
            if self.n % i == 0:
                yield i
                if i != limit and i != 1:
                    yield int(self.n / i)


def sum_of_divisors(n):
    """Returns sum of all proper divisors of n"""
    sum = 0

    for divisor in Divisors(n):
        sum += divisor

    return sum


def main():
    """
    Find all amicable numbers below N and sum them.
    Prints sum to stdout.
    """
    sum_of_amicable_numbers = 0

    for j in range(1, N):
        j_div_sum = sum_of_divisors(j)
        if j_div_sum > j:
            if sum_of_divisors(j_div_sum) == j:
                sum_of_amicable_numbers += (j + j_div_sum)

    print(sum_of_amicable_numbers)

if __name__ == '__main__':
    main()
