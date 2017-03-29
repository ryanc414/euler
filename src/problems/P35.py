#!/usr/bin/env python
"""
Circular Primes
"""
from P30 import digits
from tools.primes import prime_sieve

UPPER_LIMIT = int(1e6)


def main():
    """Count number of circular primes."""
    return len(find_circular_primes())


def find_circular_primes():
    circular_primes = set()
    prime_map = prime_sieve(UPPER_LIMIT)
    for num, is_prime in prime_map.items():
        if is_prime and num not in circular_primes:
            prime_rotations = set()
            for rot in rotations(num):
                if not prime_map[rot]:
                    break
                else:
                    prime_rotations.add(rot)
            else:
                for prime_rot in prime_rotations:
                    circular_primes.add(prime_rot)
    return circular_primes


def rotations(n):
    def rotate(digit_list, length):
        rotation = [None for _ in range(length)]
        for j in range(length):
            if j < length - 1:
                rotation[j + 1] = digit_list[j]
            else:
                rotation[0] = digit_list[j]
        return rotation

    def convert_list_to_int(int_list):
        """Converts a list of integer digits to an integer."""
        j = 0
        ans = 0
        for num in int_list[::-1]:
            ans += num * (10 ** j)
            j += 1
        return ans

    n_digits = list(digits(n))[::-1]
    limit = len(n_digits)
    for i in range(limit):
        n_digits = rotate(n_digits, limit)
        yield convert_list_to_int(n_digits)




if __name__ == '__main__':
    print(main())
