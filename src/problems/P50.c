#include <P50.h>

int main()
{
    primes = prime_sieve(&num_primes, LIMIT);
    printf("%d can be written as the sum of the most primes.\n",
            max_consec_prime_sum());

    return 0;
}


/* Find the max number of consecutive primes that add to give a prime below
 * LIMIT, returning the value of this prime. */
int max_consec_prime_sum(void)
{
    int i, j, sum, max_terms = 0, max_prime = 0;

    for (i = 0; i < num_primes; i++) {
        sum = 0;
        for (j = 0; sum < LIMIT && i + j < num_primes; j++) {
            sum += primes[i + j];
            if (IS_PRIME(sum))
                if (j > max_terms) {
                    max_terms = j;
                    max_prime = sum;
                }
        }
    }

    return max_prime;
}

