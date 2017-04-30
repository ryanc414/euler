#!/usr/bin/env python

import unittest
from subprocess import Popen, PIPE
from collections import namedtuple
from time import sleep


class TestProblems(unittest.TestCase):
    """Tests for the problems."""
    # Test parameters
    NUM_TESTS = 64
    NUM_WORKERS = 2
    POLL_TIME = 0.1

    # Shell commands to run the tests.
    COMMANDS = [['./bin/P{}'.format(i + 1)] for i in range(NUM_TESTS)]

    # Append any extra args required e.g. to specify input files
    COMMANDS[7].append("data/P8_bignum.txt")
    COMMANDS[10].append("data/P11_grid.txt")
    COMMANDS[12].append("data/P13_numbers.txt")
    COMMANDS[17].append("data/P18_triangle.txt")
    COMMANDS[21].append("data/p022_names.txt")
    COMMANDS[41].append("data/p042_words.txt")
    COMMANDS[53].append("data/p054_poker.txt")
    COMMANDS[58].append("data/p059_cipher.txt")

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
        "Sum of primes less than 2000000 is 142913828922",
        "Max product is: 70600674",
        "First triangle number to have over 500 divisors: 12375th number is 76576500 and has 576 divisors.",
        "5537376230",
        "Longest starter was 837799",
        "137846528820",
        "1366",
        "Total number of letters is 21124",
        "1074",
        "171",
        "648",
        "31626",
        "871198282",
        "4179871",
        "2783915460",
        "4782",
        "983",
        "-59231",
        "669171001",
        "9183",
        "443839",
        "73682",
        "Sum of pandigital products is 45228",
        "1 / 100",
        "Sum of digit factorials is 40730",
        "55",
        "872187",
        "Sum of truncatable primes is 748317",
        "Largest 1 to 9 pandigital formed is: 932718654",
        "Max solutions for p = 840",
        "Product of all target digits: 210",
        "7652413 is prime",
        "There are 162 triangular words.",
        "The sum of pandigitals that meet the criteria is 16695334890",
        "Smallest D is 5482660",
        "1533776805 is triangular, pentagonal and hexagonal.",
        "5777 violates the conjecture.",
        "First number is: 134043",
        "9110846700",
        "148748178147\n296962999629",
        "997651 can be written as the sum of the most primes.",
        "('121313', (0, 2, 4))",
        "142857",
        "4075",
        "Player 1 wins 376 hands",
        "249",
        "972",
        "153",
        "Side length: 26241",
        "107359",
        "[13, 5197, 5701, 6733, 8389]\nSum of lowest set: 26033",
        "deque([8256, 5625, 2512, 1281, 8128, 2882])\nSum of lowest set: 28684",
        "Set found: {589323567104, 569310543872, 373559126408, 352045367981, 127035954683}\n"
        "Lowest member of set is: 127035954683",
        "Sum: 49",
        "1322"
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
        self.assertEqual(stdout, self.EXPCT_RESULTS[test.index],
                         "Test {} failed".format(test.index + 1))
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

