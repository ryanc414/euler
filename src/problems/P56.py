#!/usr/bin/env python

"""P56: Powerful digit sum

For numbers a^b where a, b < 100, find the maximal digit sum."""

LIMIT = 100


def main():
    """Find the max digit sum."""
    max_digit_sum = 0
    
    for a in range(LIMIT):
        for b in range(LIMIT):
            new_digit_sum = digit_sum(pow(a, b))
            if new_digit_sum > max_digit_sum:
                max_digit_sum = new_digit_sum

    return max_digit_sum


def digit_sum(n):
    """Return the digit sum of a number."""
    return sum(int(d) for d in str(n))


if __name__ == '__main__':
    print main()

