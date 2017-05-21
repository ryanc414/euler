#!/usr/bin/env python3
"""Sum of amicable numbers less than 10000"""
from num_funcs import sum_of_divisors

N = 10000


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
