#!/usr/bin/env python3
"""Factorial digit sum"""
from digits import sum_digits
from math import factorial
from sys import argv, exit

N = 100


if __name__ == '__main__':
    print(sum_digits(factorial(N)))

