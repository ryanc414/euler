#!/usr/bin/env python
#!/usr/bin/python

DIGITS = 10
LIMIT = 1000

class LastNDigits(object):
    def __init__(self, n, digits):
        self.n = n % pow(10, digits)

    def __add__(self, other):
        return LastNDigits(self.n + other, DIGITS)

    def __str__(self):
        return format(self.n)


def main():
    total = LastNDigits(0, DIGITS)
    
    for i in range(1, LIMIT + 1):
        total += pow(i, i)

    return total


if __name__ == '__main__':
    print main()

