#include <problems.h>

#define LIMIT 1000000
#define IS_PRIME(n) (binsearch((long)(n), (long *)primes, num_primes) != num_primes)

int max_consec_prime_sum(void);

static unsigned long *primes;
unsigned long num_primes;
