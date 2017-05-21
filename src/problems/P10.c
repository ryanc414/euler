/* P10 - Sum of all primes below N. */

#include <P10.h>


int main(void)
{
   uint32_t num_primes;
   uint32_t i;
   uint32_t *primes;
   uint64_t sum_primes = 0;

   primes = prime_sieve(&num_primes, N);

   for (i = 0; i < num_primes; i++)
       sum_primes += primes[i];

   printf("Sum of primes less than %lu is %" PRIu64 "\n", N, sum_primes);

   return 0;
}

