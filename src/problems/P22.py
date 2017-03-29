#!/usr/bin/env python
"""Names scores"""
from sys import argv
from string import ascii_uppercase


values = {}
i = 1
for letter in ascii_uppercase:
    values[letter] = i
    i += 1


def read_and_sort(path):
    """
    Read names from file, split into list and strip all double quotes.
    :return str: list of names sorted alphabetically.
    """
    with open(path) as f:
        return sorted(name.strip('"') for name in (f.read()).split(','))


def get_score(name, position):
    """Get the score of a name in a given position."""
    score = 0

    for char in name:
        score += values[char]

    return score * position


def get_total_score(sorted_names):
    """
    Iterate through all names in list, adding the score of each to the total.
    :return int: total score of all names
    """
    total_score = 0
    position = 1

    for name in sorted_names:
        total_score += get_score(name, position)
        position += 1

    return total_score


def main():
    """
    Read and sort names from file, then print the total of all name scores
    to stdout.
    """
    if len(argv) > 1:
        try:
            print(get_total_score(read_and_sort(argv[1])))
        except IOError:
            print("Error reading specified path.")
    else:
        print("Error, path must be specified on command line.")


if __name__ == '__main__':
    main()
