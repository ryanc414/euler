#!/usr/bin/env python
"""P9: special pythagorean triplet"""

import sys

N = 1000


def find_special_pythagorean_triplet(N):
    """find abc for a^2 + b^2 = c^2 and a + b + c = 1000, a < b < c"""
    for a in range(1, N + 1):
		for b in range(a + 1, N + 1):
			try:
				c = get_c(a, b)
				if a + b + c == N:
					return (a, b, c)
			except CannotFindCException:
				pass
    else:
        print("FAIL")
        sys.exit(1)


class CannotFindCException(Exception):
	"""Exception raised when no valid c is found"""
	pass


def get_c(a, b):
	"""Return c for a^2 + b^2 = c^2"""
	for c in range(1, N + 1):
		if c * c == a * a + b * b:
			return c
	else:
		raise CannotFindCException("a = {0}, b = {1}".format(a, b))


def print_results(a, b, c):
	"""Print a, b, c in readable format"""
	print("a = {0}, b = {1}, c = {2}".format(a, b, c))
	print("Product abc = {0}".format(a * b * c))


if __name__ == '__main__':
	print_results(find_special_pythagorean_triplet(N))

