#!/usr/bin/env python

import unittest
from subprocess import Popen, PIPE
from collections import namedtuple
from time import sleep


class TestProblems(unittest.TestCase):
    """Tests for the problems."""
    NUM_TESTS = 10
    NUM_WORKERS = 2
    POLL_TIME = 0.1

    # Shell commands to run the tests.
    COMMANDS = [['./bin/P{}'.format(i + 1)] for i in range(NUM_TESTS)]

    # Append any extra args required e.g. to specify input files
    COMMANDS[7].append('data/P8_bignum.txt')

    # Expected stdout of each command
    EXPCT_RESULTS = [
        "233168",
        "4613732",
        "Largest prime factor is 6857",
        "Largest palindromic product: 906609",
        "Smallest integer divisible by all integers 1-20: 232792560",
        "25164150",
        "10,001st prime: 104743",
        "Largest product of 13 adjacent digits is 23514624000.",
        "a = 200, b = 375, c = 425\nProduct abc = 31875000",
        "Sum of primes less than 2000000 is 142913828922"
        ]

    TEST = namedtuple("Test", ["process", "index"])

    def setUp(self):
        """Sanity check that the tests have been set up correctly."""
        assert len(self.EXPCT_RESULTS) == self.NUM_TESTS
        self.tests = []
        self.next_test = 0

    def check_test(self, test):
        """Check whether the test has passed by comparing its stdout to what
        is expected."""
        (stdout, stderr) = test.process.communicate()
        self.assertFalse(stderr, stderr)
        stdout = stdout.strip().decode('ascii')
        self.assertEqual(stdout, self.EXPCT_RESULTS[test.index])
        print("Test {} passed".format(test.index + 1))

    def start_tests(self):
        """Start initial tests."""
        for _ in range(self.NUM_WORKERS):
            self.tests.append(
                self.TEST(
                    process=Popen(self.COMMANDS[self.next_test],
                                  stdout=PIPE,
                                  stderr=PIPE),
                    index=self.next_test))
            self.next_test += 1

    def poll_tests(self):
        """Poll tests for completion. When one finishes, start another one if
        there are more to run. Stop when all are finished."""
        for i, test in enumerate(self.tests):
            if test.process.poll() is not None:
                self.check_test(test)
                self.tests.pop(i)
                if self.next_test < self.NUM_TESTS:
                    self.tests.append(
                        self.TEST(
                            process=Popen(self.COMMANDS[self.next_test],
                                          stdout=PIPE,
                                          stderr=PIPE),
                            index=self.next_test))
                    self.next_test += 1

    def test_all(self):
        """Run all tests."""
        self.start_tests()
        while self.tests:
            self.poll_tests()
            sleep(self.POLL_TIME)


if __name__ == '__main__':
    unittest.main()
