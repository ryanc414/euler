#!/usr/bin/env python3

import unittest
import itertools
from functools import partial
import digits
import num_funcs
import fibonacci
import primes
import iterable_nums
import tree


class TestDigits(unittest.TestCase):
    """Tests for the digits.py module."""
    def test_sum_digits(self):
        self.assertEqual(digits.sum_digits(0), 0)
        self.assertEqual(digits.sum_digits(7), 7)
        self.assertEqual(digits.sum_digits(123), 6)
        self.assertEqual(digits.sum_digits(123456789), 45)

    def test_get_reverse_digits(self):
        self.assertEqual(list(digits.gen_reverse_digits(0)), [0])
        self.assertEqual(list(digits.gen_reverse_digits(7)), [7])
        self.assertEqual(list(digits.gen_reverse_digits(123)), [3, 2, 1])
        self.assertEqual(list(digits.gen_reverse_digits(987654321)),
                         [1, 2, 3, 4, 5, 6, 7, 8, 9])


class TestFibonacci(unittest.TestCase):
    """Tests for the Fibonacci class."""
    def test_fibonacci_series(self):
        fib = fibonacci.FibonacciSeries()
        fib_seq = [n.value for n in itertools.islice(fib, 9)]
        self.assertEqual(fib_seq, [1, 1, 2, 3, 5, 8, 13, 21, 34])


class TestNumFuncs(unittest.TestCase):
    """Tests for the num_funcs.py module."""
    def test_sum_of_divisors(self):
        self.assertEqual(num_funcs.sum_of_divisors(0), 0)
        self.assertEqual(num_funcs.sum_of_divisors(1), 1)
        self.assertEqual(num_funcs.sum_of_divisors(12), 16)

    def test_gen_ints_of_len(self):
        self.assertEqual(num_funcs.gen_ints_of_len(1), range(1, 10))
        self.assertEqual(num_funcs.gen_ints_of_len(2), range(10, 100))


class TestPrimes(unittest.TestCase):
    """Tests for the primes.py module."""
    def test_prime_sieve(self):
        self.assertEqual(primes.prime_sieve(1), set())
        self.assertEqual(primes.prime_sieve(10), set([2, 3, 5, 7]))

    def test_is_prime(self):
        self.assertFalse(primes.is_prime(0))
        self.assertFalse(primes.is_prime(1))
        self.assertTrue(primes.is_prime(2))
        self.assertTrue(primes.is_prime(3))
        self.assertTrue(primes.is_prime(7))
        self.assertFalse(primes.is_prime(100))
        self.assertTrue(primes.is_prime(2357))


class TestIterableNums(unittest.TestCase):
    """Tests for the iterable_nums.py module."""
    def test_iterable_int(self):
        x = iterable_nums.IterableInt(123)
        self.assertEqual(x.digits, [1, 2, 3])
        self.assertEqual(x.n, 123)


class TestTree(unittest.TestCase):
    """Tests for the tree.py module."""
    def test_tree(self):
        """Set up a basic test tree and look for values in it."""
        root = tree.Node(0)
        root.children = [tree.Node(1), tree.Node(2)]
        root.children[0].children = [tree.Node(3), tree.Node(4)]

        self.assertRaises(
            tree.Found,
            tree.traverse_dfs,
            root,
            callback=partial(tree.lookup, 4))

        # Should not raise anything
        tree.traverse_dfs(root, callback=partial(tree.lookup, 10))

        self.assertRaises(
            tree.Found,
            tree.traverse_bfs,
            root,
            callback=partial(tree.lookup, 4))

        # Should not raise anything
        tree.traverse_bfs(root, callback=partial(tree.lookup, 10))


if __name__ == '__main__':
    unittest.main()

