#!/usr/bin/env python
"""P65 - Find the sum of the digits in the numerator of the 100th continued
fraction approximation of e.

e is given by the continued fraction
e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...]"""

def find_numerator(x, n):
    """Find the numerator of the nth term in the continued fraction using
    coefficients x_i. Note that we calculate terms from i = 0 to i = n
    inclusive."""
    a = [x[n]]
    b = [1]

    for i in range(1, n + 1):
        b.append(a[i - 1])
        a.append((x[n - i ] * a[i - 1]) + b[i - 1])

    return a[-1]


def fill_x(n):
    """Fill x_0 to x_n of the coefficients required for the continued fraction
    approximation to e."""
    x = [2]

    for i in range(n):
        if i % 3 == 1:
            x.append(2 * (i // 3 + 1))
        else:
            x.append(1)

    return x

def main():
    """Find the sum of the 100th continued fraction numerator in the expansion
    of e. Note we start from n = 0 so we actually look for the n = 99 term."""
    n = 99

    x = fill_x(n)

    print("{}th approx to e's digit sum = {}".format(
        n + 1, sum(int(d) for d in str(find_numerator(x, n)))))


if __name__ == '__main__':
    main()

