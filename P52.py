#!/usr/bin/env python

LIMIT = int(1e11)
MULTIPLES = range(2, 7)

def main():
    for i in xrange(1, LIMIT):
        for m in MULTIPLES:
            if not contain_same_digits(i, m * i):
                break
        else:
            return i


def contain_same_digits(x, y):
    return sorted(str(x)) == sorted(str(y))


if __name__ == '__main__':
    print main()
