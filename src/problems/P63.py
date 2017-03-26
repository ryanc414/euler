#!/usr/bin/env python
"""P63 - Powerful Digit Counts"""

def main():
    """Count the total number of n-digit integers x such that x = y^n for some
    y and n."""



def count_digit_powers():
    """Count the number of n-digit integers x such that x = y^n for some y
    and fixed n."""
    y = 1
    lower_limit = 1
    upper_limit = 10
    count = 0
    n = 1

    while True:
        x = y ** n
        y += 1
        if x > upper_limit:
            print "{0}: {1}".format(n, count)
            if not count:
                break
            yield count
            count = 0
            lower_limit = upper_limit
            upper_limit *= 10
            n += 1
            continue
        if x >= lower_limit:
            count += 1


if __name__ == '__main__':
    main()

