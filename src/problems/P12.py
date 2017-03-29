#!/usr/bin/env python
"""
Highly divisible triangle numbers
"""

def find_num_divisors(n):
    """
    Finds the number of divisors of an integer n
    """
    if n <= 1:
        return n
    num_divisors = 1
    i = 2
    count = 0
    limit = n ** 0.5
    while True:
        if i > limit:
            if i != n:
                # count previous factor
                num_divisors *= (count + 1)
                count = 0
            count += 1
            num_divisors *= (count + 1)
            break
        elif n % i == 0:  # found a factor
            n /= i
            limit = n ** 0.5
            count += 1
        else:
            # i is not a factor, so increment
            if i == 2:
                i += 1
            else:
                i += 2
            num_divisors *= count + 1
            count = 0

    return num_divisors


def main():
    """
    Finds first triangle number to have more than the target number
    of divisors.
    """
    N = int(1e6)
    target_divisors = 500
    n = 0

    for i in range(1, N+1):
        num_divisors = find_num_divisors(n)
        n += i
        if num_divisors > target_divisors:
            print(("First triangle number to have over {3} divisors:"
                  " {0}th number is {1} and has {2} divisors.".format(
                i, n, num_divisors, target_divisors
            )
                   ))
            break
    else:
        print("FAIL: maybe make N bigger?")


if __name__ == '__main__':
    main()