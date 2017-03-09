#!/usr/bin/env python

from math import sqrt, floor
from itertools import count

N = 10000 


class ContinuedFraction(object):
    """An irrational square root can be written as a series of continuous
    fractions as follows:

    sqrt(n) = a0 + 1 / (a1 + 1 / (a2 + ...))

    This always results in a series ai that is periodic from some starting
    index i."""
    def __init__(self, n):
        self.n = int(n)

    def find_period(self):
        """Finds the period of the sequence ai of the continuous fraction
        coefficients."""
        if self._is_square():
            return 0 
        
        b = [0]
        c = [1]
        n = self.n

        for i in count():
            x = (sqrt(n) + b[i]) / c[i]
            a = int(x)
            b.append(c[i] * a - b[i])
            c.append((n - (b[i] - c[i] * a) ** 2) / c[i])
            period = self.repeated_coeffs(b, c, i)
            if period:
                return period
            
    @staticmethod
    def repeated_coeffs(b, c, i):
        """Find if we have repeated a set of i coefficient pairs b and c. If
        so, then the period of repetition can be returned."""
        for j in range(i):
            if b[j] == b[i] and c[j] == c[i]:
                return i - j
        return None

    def _is_square(self):
        """If we are a perfect square, we can't be a continued fraction.
        Check for this early."""
        x = sqrt(self.n)
        return x == floor(x)


def is_odd(n):
    """Returns True if integer n is odd."""
    return bool(n % 2)

if __name__ == '__main__':
    print sum(1 for i in range(1, N + 1) 
              if is_odd(ContinuedFraction(i).find_period()))

