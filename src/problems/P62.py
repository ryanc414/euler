#!/usr/bin/env python3
"""P62 - Cubic Permutations"""

REQUIRED_PERMS = 5 


def main():
    """Find the lowest cube for which 5 of the permutations of its digits are
    also cubes."""
    try:
        search_cubes()
    except SetFound as e:
        print("Lowest member of set is: {0}".format(min(e.result)))


class SetFound(Exception):
    """Signal raised when a set is found."""
    def __init__(self, result):
        self.result = result
        super(SetFound, self).__init__()


def search_cubes():
    """Builds up lists of cubes containing the same numbers of digits. For
    each such list, look for the required number of permutations."""
    limit = 10
    cubes = []
    
    for n in iter_cubes():
        if n < limit:
            cubes.append(n)
        else:
            limit *= 10
            find_permutations(cubes)
            cubes = [n]


def find_permutations(cubes):
    """Given a list of cubes with the same number of digits, look for a set of
    REQUIRED_PERMS size that all share digits."""
    x_ref_cubes = set(cubes)

    for x in cubes:
        if x not in x_ref_cubes:
            # We've already failed to find enough permutations for this cube,
            # so don't try again!
            continue

        possible_set = set([x])
        x_ref_cubes.remove(x)
        
        # Out of the remaining cubes, find how many are permutations of x.
        for y in x_ref_cubes:
            if share_digits(x, y):
                possible_set.add(y)
        
        if len(possible_set) == REQUIRED_PERMS:
            raise SetFound(possible_set)
        else:
            # Not the right number of permutations were found. Disregard all
            # permutations so we don't check them again.
            x_ref_cubes -= possible_set


def share_digits(x, y):
    """Return True if x and y contain the same digits."""
    return sorted(str(x)) == sorted(str(y))


def iter_cubes():
    """Iterate through all cubes."""
    def cube(x):
        return x ** 3
    
    i = 1

    while True:
        yield cube(i)
        i += 1


if __name__ == '__main__':
    main()

