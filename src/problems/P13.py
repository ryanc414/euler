#!/usr/bin/env python
"""
Problem 13: Large Sum
"""
from sys import argv
import math

result_digits = 10  # number of digits we care about

class LongNumbers(object):
    """
    Describes a set of very  loooooooooooooong numbers.
    """
    def __init__(self, num_digits):
        """
        Caller tells us how many digits to care about.
        """
        self.num_digits = num_digits

    def main(self):
        """
        Read the numbers and print their truncated sum.
        """
        try:
            self.read_numbers(argv[1])
        except IndexError:
            print "Error: must specify file"
        except IOError:
            print "Error: could not read file"
        else:
            print self.add_all_numbers()

    def read_numbers(self, filename):
        """
        Read numbers in from a plaintext file.
        Raises IOError if file can't be read.
        :param filename str: name or path of file to open
        :return list(int): list of integers, each truncated to
        the min_length needed.
        """
        with open(filename) as f:
            self.find_min_length(
                self.file_len(f)
            )
            f.seek(0)
            self.num_list = [
                self.first_n_digits(
                    num.strip(), self.min_length) for num in f
                ]
            self.num_lines = len(self.num_list)

    def add_all_numbers(self):
        """
        Add all the numbers!
        :return int: the sum, truncated to the number of digits we care about.
        """
        sum = self.num_list[0]
        for i in range(1, self.num_lines):
            sum += self.num_list[i]

        return self.first_n_digits(sum, self.num_digits)

    @staticmethod
    def file_len(f):
        """
        Find length of a file
        :param f: file object
        :return int: length of file
        """
        i = 0
        for i, l in enumerate(f):
            pass
        return i + 1

    def find_min_length(self, num_lines):
        """
        Find the minimum length each number has to be
        so that we don't get rounding errors.
        """
        self.min_length = self.num_digits + int(
           math.log10(num_lines)
        )

    def first_n_digits(self, num, N):
        """
        Returns the first N digits of a number formatted as a string,
        returned as an integer.
        :param num str: input number formatted as a string
        :param N int: number of leading digits desired
        :return int: first N digits of input
        """
        num = self.convert_string_to_int_list(str(num))
        while len(num) > N:
            num.pop(-1)
        return self.convert_list_to_int(num)

    @staticmethod
    def convert_string_to_int_list(string):
        """
        Convert a string to a list of integer digits.
        :param string str:
        :return list(int): each integer will be a digit 0-9
        """
        return [int(char) for char in string]

    def print_numbers(self):
        """
        Print all the numbers for debugging purposes.
        """
        for num in self.num_list:
            print num

    @staticmethod
    def convert_list_to_int(list):
        """
        Converts a list of integer digits to an integer.
        """
        i = 0
        ans = 0
        for num in list[::-1]:
            ans += num * (10 ** i)
            i += 1
        return ans

if __name__ == '__main__':
    my_numbers = LongNumbers(result_digits)
    my_numbers.main()

