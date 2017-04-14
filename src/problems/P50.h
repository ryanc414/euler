#include <problems.h>

#define LIMIT 1000000
#define IS_PRIME(n) (binsearch((n), primes, num_primes) >= 0)

int max_consec_prime_sum(void);
int prime_sieve(int **primes, int limit);
int binsearch(int val, int *array, int lim);

static int *primes;
static int num_primes;
