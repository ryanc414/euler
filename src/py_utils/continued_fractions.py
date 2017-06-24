#!/usr/bin/env python3
"""Provide classes to help with using continued fraction representations of
irrational numbers."""

import math
import itertools
import num_funcs


class ContinuedFractionSqRoot(object):
    """A continued fraction representation of an irrational square root is
    characterised by coefficients a_i such that the square root of n is:

    sqrt(n) = a_0 + 1 / (a_1 + 1 / (a_2 + ...)) for i = 0 -> infinity.

    The coefficients a_i will always be periodic for some value a_{r+1} = 2a_0.

The nth approximation to the square root is given by the fraction p_n/q_n.
Values P and Q are also calculated to assist in calculating the values of a, p
and q."""
    def __init__(self, n):
        self.n = n
        self.period = None
        self.P = None
        self.Q = None
        self.a = None
        self.p = None
        self.q = None
        self.is_square = num_funcs.is_square(n)

    def find_coeffs(self):
        """Find the continued fraction coefficients a_i by calculating the
        related coefficients P_i and Q_i. Stop when the coefficients
        become periodic."""
        if self.is_square:
            self.period = 0
            return

        n = self.n

        a = [int(math.floor(math.sqrt(n)))]
        P = [0]
        Q = [1]

        for i in itertools.count(1):
            P.append(a[i - 1] * Q[i - 1] - P[i - 1])
            Q.append((n - P[i] * P[i]) // Q[i - 1])
            a.append((a[0] + P[i]) // Q[i])
            period = self.repeated_coeffs(P, Q, i)
            if period:
                P.pop()
                Q.pop()
                a.pop()
                break

        self.period = period
        self.P = P
        self.Q = Q
        self.a = a

    def find_period(self):
        if self.period is None:
            self.find_coeffs()
        return self.period

    def find_partial_fracs(self, limit):
        """Find the partial fraction coefficients p_i and q_i such that the
        nth approximation to sqrt(n) is p_n / q_n."""
        if self.is_square:
            return

        if not self.a:
            self.find_coeffs()
            assert(self.a)

        a = self.a

        p = [a[0], a[0] * a[1] + 1]
        q = [1, a[1]]

        for j in range(2, limit + 1):
            i = ((j - 1) % self.period) + 1
            p.append(a[i] * p[j - 1] + p[j - 2])
            q.append(a[i] * q[j - 1] + q[j - 2])

        self.p = p
        self.q = q

    @staticmethod
    def repeated_coeffs(b, c, i):
        """Find if we have repeated a set of i coefficient pairs b and c. If
        so, then the period of repetition can be returned."""
        for j in range(i + i):
            if b[j] == b[i] and c[j] == c[i]:
                return i - j
        return None

