#!/usr/bin/env python3
"""P4: largest palindromic product of two 3-digit nums."""

LOWER_LIMIT = 100
UPPER_LIMIT = 1000


def main():
    largest_palindrome = 0 

    for i in range(LOWER_LIMIT, UPPER_LIMIT):
        for j in range(i, UPPER_LIMIT):
            product = i * j
            if is_palindrome(product) and product > largest_palindrome:
                largest_palindrome = product

    return largest_palindrome


def is_palindrome(num):
    numstr = str(num)
    return numstr == numstr[::-1]


if __name__ == '__main__':
    print(("Largest palindromic product: {}".format(main())))

