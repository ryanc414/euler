#!/usr/bin/env python
"""Even Fibonacci numbers"""

from P25 import FibonacciNumbers

MAX_VALUE = int(4e6)


def main():
    """Sum even Fibonacci terms below 4 million."""
    sum_terms = 0
    for term in FibonacciNumbers(1, 2):
        if term.value <= MAX_VALUE:
            if term.value % 2 == 0:
                sum_terms += term.value
        else:
            break
    print sum_terms


if __name__ == '__main__':
    main()
