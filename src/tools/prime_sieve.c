#include <math.h>
#include <stdlib.h>

int prime_sieve(int **primes, int limit)
{
    int i, j, num_primes = 0, sqrt_limit = (int) sqrt(limit);
    char prime_bool[limit];

    /* Initialise the bool array. */
    for (i = 2; i < limit; i++)
        prime_bool[i] = 1;

    /* Set each non-prime to 0. */
    for (i = 2; i <= sqrt_limit; i++)
        if (prime_bool[i])
            for (j = i * i; j <= limit; j += i)
                prime_bool[j] = 0;

    /* Count the number of  primes. */
    for (i = 2; i < limit; i++)
        if (prime_bool[i])
            num_primes++;

    /* Allocate memory for the primes. */
    *primes = malloc(num_primes * sizeof(int));

    /* Add all primes out to output array. */
    for (i = 2, j = 0; i < limit; i++)
       if (prime_bool[i])
           (*primes)[j++] = i;

    return num_primes;
}

