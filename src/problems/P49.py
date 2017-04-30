#!/usr/bin/env python

from itertools import permutations
from primes import prime_sieve

NUM_DIGITS = 4
NUM_TERMS = 3


def main():
    results = set()
    for prime_permutations in PermutePrimes(NUM_DIGITS):
        if len(prime_permutations) >= NUM_TERMS:
            for p in (sorted(perm) for perm in
                    permutations(prime_permutations, NUM_TERMS)):
                if arith_seq_exists(p):
                    results.add(concat_list(p))
    return results


class PermutePrimes(object):
    def __init__(self, digits):
        self.primes = set(prime for prime in prime_sieve(pow(10, digits))
                          if prime > pow(10, digits - 1))

    def __iter__(self):
        for prime in self.primes:
            yield [num for num in UniquePermuteNums(prime) if num in self.primes]


class UniquePermuteNums(object):
    def __init__(self, n):
        self.n = str(n)

    def __iter__(self):
        return (num for num in set(self.tuple_to_int(n) for n in permutations(self.n)))

    @staticmethod
    def tuple_to_int(tup):
        result = 0
        for term in tup:
            result = result * 10 + int(term)
        return result


def arith_seq_exists(nums):
    return nums[1] - nums[0] == nums[2] - nums[1]


def concat_list(nums):
    return int(''.join(str(n) for n in nums))


if __name__ == '__main__':
    for res in main():
        print(res)

