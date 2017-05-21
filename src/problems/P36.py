#!/usr/bin/env python3
"""
Double-base Palindromes

Finds the sum of all numbers less than 1 million that are
palindromes in both bases 10 and 2.
"""
UPPER_LIMIT = int(1e6)


def main():
    """Sum all double-base palindromes below UPPER_LIMIT."""
    return sum(double_base_palindromes())


def double_base_palindromes(): 
    """
    Generate all double-base palindromes below UPPER_LIMIT.
    We only need to check odd numbers, since all even numbers
    will not be palindromes in binary.
    """
    for n in range(1, UPPER_LIMIT, 2):    
        if is_palindrome(n) and is_palindrome(binary(n)): 
            yield n


def is_palindrome(n):
    """Check if n is a palindrome."""
    n = str(n)
    return n == n[::-1]


def binary(n):
    """
    Convert decimal n to binary representation.
    Leading '0b' from built-in bin() is cut.
    """
    return bin(n)[2::]


if __name__ == '__main__':
    print(main())

