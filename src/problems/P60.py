#!/usr/bin/env python3
"""Project Euler Problem 60 - Prime Pair Sets"""

from primes import prime_sieve, is_prime
from tree import Found, Node, traverse_dfs

N = 5 
UPPER_LIMIT = int(1e4)


def main():
    """Find the lowest sum of a set of 5 primes for which each pair
    concatenates to form other primes."""
    primes = sorted(prime_sieve(UPPER_LIMIT))

    lowest_set = find_lowest_set(primes)

    print(lowest_set)
    print("Sum of lowest set: {}".format(sum(int(p.val) for p in lowest_set)))


def find_lowest_set(primes):
    """Finds a set of 5 primes where each pair concatenates to form another
    prime. Assume that these are rare enough for us to find the one with the
    lowest sum first."""
    def check_prime(prime_node, possible_set):
        """Callback function for depth first search algorithm.""" 
        p = prime_node.val

        for q in possible_set:
            if p == q or not concats_to_prime(p, q):
                return False
        
        if len(possible_set) == N - 1:
            possible_set.append(prime_node)
            raise Found()

        prime_node.children = prime_nodes

        return True

    prime_nodes = [Node(p) for p in primes]
    
    try:
        for pnode in prime_nodes:
            possible_set = []
            traverse_dfs(pnode, possible_set, check_prime) 
    except Found:
        return possible_set
    else:
        raise Exception("Couldn't find a big enough set.")


def concats_to_prime(p, q):
    """Decide if a pair of primes mutually concatenates to form two different
    primes."""
    return (is_prime(int(str(p) + str(q))) and
            is_prime(int(str(q) + str(p))))


if __name__ == '__main__':
    main()

