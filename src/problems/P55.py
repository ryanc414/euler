#!/usr/bin/env python
"""P55: find the number of Lychrel numbers below 10000.

A Lychrel number produces no palindromes through any number
of iterations of the reverse-add process (adding the number
to its reverse). For the purposes of the problem, assume that
any number that isn't palindromic after 50 iterations is a
Lychrel."""


LIMIT = 10000
MAX_ITERATIONS = 50


def main():
    """Count the number of Lychrel numbers below LIMIT."""
    lyc_count = 0

    for i in range(1, LIMIT):
        n = i
        for _ in range(MAX_ITERATIONS):
            n = reverse_add(n)
            if is_palindrome(n):
                break
        else:
            # Found a Lychrel number
            lyc_count += 1
    
    return lyc_count


def reverse_add(n):
    """Add a number to its reverse (digit order reversed)."""
    n = str(n)
    return int(n) + int(n[::-1])


def is_palindrome(n):
    """Check if a number is a palindrome (equal to its reverse)."""
    n = str(n)
    return n == n[::-1]


if __name__ == '__main__':
    print(main())

