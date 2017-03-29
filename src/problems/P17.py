#!/usr/bin/env python
"""
Number letter counts
"""


class WordyNumbers(object):
    numbers = {
        1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
        6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
        10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
        14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
        17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
        20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
        60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety',
        100: 'hundred', 1000: 'thousand', '+': 'and'
    }

    def __init__(self, n):
        self.n = n

    def convert_number_to_word(self, n):
        digits = str(n)
        length = len(digits)
        if length == 1:
            return self.numbers[n]
        elif length == 2:
            return self.convert_tens(n)
        elif length == 3:
            return self.convert_hundreds(n)
        elif length == 4:
            return self.convert_thousand(n)
        else:
            raise ValueError

    def convert_tens(self, n):
        if n in self.numbers:
            return self.numbers[n]
        else:
            tens = int(n / 10)
            return self.numbers[10 * tens] + self.numbers[n % 10]

    def convert_hundreds(self, n):
        hundreds = int(n / 100)
        if n % 100 == 0:
            return self.numbers[hundreds] + self.numbers[100]
        result = (
            self.numbers[hundreds] + self.numbers[100]
            + self.numbers['+']
            + self.convert_tens(n - (100 * hundreds))
        )
        return result

    def convert_thousand(self, n):
        assert n == 1000
        return self.numbers[1] + self.numbers[1000]

    def __len__(self):
        return len(self.convert_number_to_word(self.n))


def count_all_letters():
    limit = 1000
    return (
        len(WordyNumbers(i)) for i in range(1, limit + 1)
    )


if __name__ == '__main__':
    sum = 0
    for count in count_all_letters():
        sum += count
    print("Total number of letters is {0}".format(sum))
