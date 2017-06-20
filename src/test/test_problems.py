#!/usr/bin/env python3

import unittest
from subprocess import Popen, PIPE
from collections import namedtuple, deque
from time import sleep
import argparse


# Test parameters
NUM_TESTS = 65
NUM_WORKERS = 2
POLL_TIME = 0.1

# Shell commands to run the tests.
COMMANDS = {i + 1: ['./bin/P{}'.format(i + 1)] for i in range(NUM_TESTS)}

# Append any extra args required e.g. to specify input files
COMMANDS[8].append("data/P8_bignum.txt")
COMMANDS[11].append("data/P11_grid.txt")
COMMANDS[13].append("data/P13_numbers.txt")
COMMANDS[18].append("data/P18_triangle.txt")
COMMANDS[22].append("data/p022_names.txt")
COMMANDS[42].append("data/p042_words.txt")
COMMANDS[54].append("data/p054_poker.txt")
COMMANDS[59].append("data/p059_cipher.txt")

# Expected stdout of each command
EXPCT_RESULTS = {
    1: "233168",
    2: "4613732",
    3: "Largest prime factor is 6857",
    4: "Largest palindromic product: 906609",
    5: "Smallest integer divisible by all integers 1-20: 232792560",
    6: "25164150",
    7: "10,001st prime: 104743",
    8: "Largest product of 13 adjacent digits is 23514624000.",
    9: "a = 200, b = 375, c = 425\nProduct abc = 31875000",
    10: "Sum of primes less than 2000000 is 142913828922",
    11: "Maximum product of four consecutive elements is 70600674",
    12: "First triangle number to have over 500 divisors: 12375th number is 76576500 and has 576 divisors.",
    13: "5537376230",
    14: "Longest starter was 837799",
    15: "137846528820",
    16: "1366",
    17: "Total number of letters is 21124",
    18: "1074",
    19: "171",
    20: "648",
    21: "31626",
    22: "871198282",
    23: "4179871",
    24: "2783915460",
    25: "4782",
    26: "983",
    27: "-59231",
    28: "669171001",
    29: "9183",
    30: "443839",
    31: "73682",
    32: "Sum of pandigital products is 45228",
    33: "1 / 100",
    34: "Sum of digit factorials is 40730",
    35: "55",
    36: "872187",
    37: "Sum of truncatable primes is 748317",
    38: "Largest 1 to 9 pandigital formed is: 932718654",
    39: "Max solutions for p = 840",
    40: "Product of all target digits: 210",
    41: "7652413 is prime",
    42: "There are 162 triangular words.",
    43: "The sum of pandigitals that meet the criteria is 16695334890",
    44: "Smallest D is 5482660",
    45: "1533776805 is triangular, pentagonal and hexagonal.",
    46: "5777 violates the conjecture.",
    47: "First number is: 134043",
    48: "9110846700",
    49: "148748178147\n296962999629",
    50: "997651 can be written as the sum of the most primes.",
    51: "('121313', (0, 2, 4))",
    52: "142857",
    53: "4075",
    54: "Player 1 wins 376 hands",
    55: "249",
    56: "972",
    57: "153",
    58: "Side length: 26241",
    59: "107359",
    60: "[13, 5197, 5701, 6733, 8389]\nSum of lowest set: 26033",
    61: "Sum of lowest set: 28684",
    62: "Lowest member of set is: 127035954683",
    63: "Sum: 49",
    64: "1322",
    65: "100th approx to e's digit sum = 272"
}

class TestProblems(unittest.TestCase):
    """Tests for the problems."""
    TEST = namedtuple("Test", ["process", "number"])

    def setUp(self):
        """Sanity check that the tests have been set up correctly."""
        assert COMMANDS.keys() == EXPCT_RESULTS.keys()
        self.tests = []
        self.test_numbers = deque(sorted(COMMANDS.keys()))

    def check_test(self, test):
        """Check whether the test has passed by comparing its stdout to what
        is expected."""
        (stdout, stderr) = test.process.communicate()
        self.assertFalse(stderr)
        stdout = stdout.strip().decode('ascii')
        self.assertEqual(stdout, EXPCT_RESULTS[test.number],
                         "Test {} failed".format(test.number))
        print("Test {} passed".format(test.number))

    def start_tests(self):
        """Start initial tests."""
        for _ in range(min(NUM_WORKERS, NUM_TESTS)):
            self.start_next_test()

    def start_next_test(self):
        """Start the next test."""
        next_test_num = self.test_numbers.popleft()
        self.tests.append(
                self.TEST(
                process=Popen(COMMANDS[next_test_num],
                              stdout=PIPE,
                              stderr=PIPE),
                number=next_test_num))

    def poll_tests(self):
        """Poll tests for completion. When one finishes, start another one if
        there are more to run. Stop when all are finished."""
        for i, test in enumerate(self.tests):
            if test.process.poll() is not None:
                self.check_test(test)
                self.tests.pop(i)
                if self.test_numbers:
                    self.start_next_test()

    def test_all(self):
        """Run all tests."""
        self.start_tests()
        while self.tests:
            self.poll_tests()
            sleep(POLL_TIME)


def parse_tests(tests_input):
    """Parse the tests to be run. These may be given as a single number,
    a comma-seperated list or two numbers seperated by a dash."""
    if '-' in tests_input:
        limits = tests_input.partition('-')
        tests = list(range(int(limits[0]), int(limits[2]) + 1))
    else:
        tests = [int(t) for t in tests_input.split(',')]

    return tests


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run tests for the problems")
    parser.add_argument("-t", "--tests", type=str,
                        help="Run specific test numbers x,y,z or in range x-z "
                             "inclusive.")
    parser.add_argument("-n", "--num_workers", type=int,
                        help="Number of threads to run tests accross.")
    args = parser.parse_args()

    if args.tests:
        try:
            tests = parse_tests(args.tests)
        except ValueError:
            print("Error, could not parse tests input {}.\n"
                  "Please enter test numbers in format x,y,z or x-z."
                  .format(args.tests))
            exit(1)

        # Only run the specified subset of the tests.
        COMMANDS = {i: COMMANDS[i] for i in tests}
        EXPCT_RESULTS = {i: EXPCT_RESULTS[i] for i in tests}
        NUM_TESTS = len(COMMANDS)

    if args.num_workers:
        assert args.num_workers > 0
        NUM_WORKERS = args.num_workers

    suite = unittest.TestLoader().loadTestsFromTestCase(TestProblems)
    unittest.TextTestRunner().run(suite)

