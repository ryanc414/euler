#!/usr/bin/env python
"""Factorial digit sum"""
from P16 import sum_digits
from math import factorial
from sys import argv, exit

N = 100


if __name__ == '__main__':
    print(sum_digits(factorial(N)))

