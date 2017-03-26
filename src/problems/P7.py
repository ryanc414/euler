# Nth prime

N = 10001
j = 1

def is_prime(n):
    """Determine if n is a prime number"""
    # first perform some sanity checks
    if not isinstance(n, int):
        return False
    if n <= 1:
        return False
    if n == 2:
        return True

    # now check for primeness
    for i in range(2, int(n ** 0.5) + 2):
        if n % i == 0:
            return False
    else:
        return True

def main():
    for i in range(1, N+1):
        j += 1
        while not is_prime(j):
            j += 1
        print "%dth prime found: %d" % (i, j)
    print j

if __name__ == '__main__':
    main()