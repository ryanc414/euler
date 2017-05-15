#include <problems.h>

#define LIMIT 1000000
#define IS_PRIME(n)                                                           \
  (bsearch(&(n), primes, num_primes, sizeof(uint32_t), comp_uint32) != NULL)

uint32_t max_consec_prime_sum(void);

static uint32_t *primes;
uint32_t num_primes;

