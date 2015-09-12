# Nth prime

N = 10001
j = 1

def is_prime(n):
    if n == 2:
        return True
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 2):
        if n % i == 0:
            return False
    return True

for i in range(1, N+1):
    j += 1
    while not is_prime(j):
        j += 1
    print "%dth prime found: %d" % (i, j)

print j
