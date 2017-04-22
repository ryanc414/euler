#!/usr/bin/env python

import  unittest
from subprocess import Popen, PIPE


class TestProblems(unittest.TestCase):
    """Tests for the problems."""
    NUM_TESTS = 10

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

    def syscall(self, cmd):
        """Make a sys call and return the stdout."""
        process = Popen(cmd, stdout=PIPE, stderr=PIPE)
        (stdout, stderr) = process.communicate()
        self.assertFalse(stderr, stderr)
        return stdout.strip().decode('ascii')

    def run_test(self, n):
        """Run a single command and check that the stdout matches the expected
        result."""
        self.assertEqual(self.syscall(self.COMMANDS[n]),
                         self.EXPCT_RESULTS[n])
        print("Test {} passed".format(n + 1))

    def test_all(self):
        """Run all tests."""
        for i in range(self.NUM_TESTS):
            self.run_test(i)


if __name__ == '__main__':
    unittest.main()

