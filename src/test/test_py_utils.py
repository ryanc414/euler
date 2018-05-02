#!/usr/bin/env python3

import itertools
from functools import partial
import digits
import num_funcs
import fibonacci
import primes
import iterable_nums
import tree
import sys

from testplan.testing.multitest import MultiTest, testsuite, testcase
from testplan import test_plan
from testplan.report.testing.styles import Style, StyleEnum

@testsuite
class TestDigits(object):
    """Tests for the digits.py module."""
    @testcase
    def test_sum_digits(self, env, result):
        result.equal(digits.sum_digits(0), 0)
        result.equal(digits.sum_digits(7), 7)
        result.equal(digits.sum_digits(123), 6)
        result.equal(digits.sum_digits(123456789), 45)

    @testcase
    def test_get_reverse_digits(self, env, result):
        result.equal(list(digits.gen_reverse_digits(0)), [0])
        result.equal(list(digits.gen_reverse_digits(7)), [7])
        result.equal(list(digits.gen_reverse_digits(123)), [3, 2, 1])
        result.equal(list(digits.gen_reverse_digits(987654321)),
                         [1, 2, 3, 4, 5, 6, 7, 8, 9])


@testsuite
class TestFibonacci(object):
    """Tests for the Fibonacci class."""
    @testcase
    def test_fibonacci_series(self, env, result):
        fib = fibonacci.FibonacciSeries()
        fib_seq = [n.value for n in itertools.islice(fib, 9)]
        result.equal(fib_seq, [1, 1, 2, 3, 5, 8, 13, 21, 34])


@testsuite
class TestNumFuncs(object):
    """Tests for the num_funcs.py module."""
    @testcase
    def test_sum_of_divisors(self, env, result):
        result.equal(num_funcs.sum_of_divisors(0), 0)
        result.equal(num_funcs.sum_of_divisors(1), 1)
        result.equal(num_funcs.sum_of_divisors(12), 16)

    @testcase
    def test_gen_ints_of_len(self, env, result):
        result.equal(num_funcs.gen_ints_of_len(1), range(1, 10))
        result.equal(num_funcs.gen_ints_of_len(2), range(10, 100))


@testsuite
class TestPrimes(object):
    """Tests for the primes.py module."""
    @testcase
    def test_prime_sieve(self, env, result):
        result.equal(primes.prime_sieve(1), set())
        result.equal(primes.prime_sieve(10), set([2, 3, 5, 7]))

    @testcase
    def test_is_prime(self, env, result):
        result.false(primes.is_prime(0))
        result.false(primes.is_prime(1))
        result.true(primes.is_prime(2))
        result.true(primes.is_prime(3))
        result.true(primes.is_prime(7))
        result.false(primes.is_prime(100))
        result.true(primes.is_prime(2357))


@testsuite
class TestIterableNums(object):
    """Tests for the iterable_nums.py module."""
    @testcase
    def test_iterable_int(self, env, result):
        x = iterable_nums.IterableInt(123)
        result.equal(x.digits, [1, 2, 3])
        result.equal(x.n, 123)


@testsuite
class TestTree(object):
    """Tests for the tree.py module."""
    @testcase
    def test_tree(self, env, result):
        """Set up a basic test tree and look for values in it."""
        root = tree.Node(0)
        root.children = [tree.Node(1), tree.Node(2)]
        root.children[0].children = [tree.Node(3), tree.Node(4)]

        with result.raises(tree.Found):
            tree.traverse_dfs(root, callback=partial(tree.lookup, 4))

        # Should not raise anything
        tree.traverse_dfs(root, callback=partial(tree.lookup, 10))

        with result.raises(tree.Found):
            tree.traverse_bfs(root, callback=partial(tree.lookup, 4))

        # Should not raise anything
        tree.traverse_bfs(root, callback=partial(tree.lookup, 10))


@test_plan(
    name='Python utils tests',
    stdout_style=Style(
        passing=StyleEnum.ASSERTION_DETAIL,
        failing=StyleEnum.ASSERTION_DETAIL
    )
)
def main(plan):
    plan.add(MultiTest(name='Python utils tests', suites=[
        TestDigits(),
        TestFibonacci(),
        TestNumFuncs(),
        TestPrimes(),
        TestIterableNums(),
        TestTree()]))


if __name__ == '__main__':
    sys.exit(not main())

