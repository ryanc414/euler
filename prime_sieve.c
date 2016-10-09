#include <stdio.h>
#include <math.h>


void prime_sieve(long int *primes, long int limit)
{
    long int i, j;
    char prime_bool[limit];

    /* Initialise the bool array. */
    for (i = 2; i < limit; i++)
        prime_bool[i] = 1;

    /* Set each non-prime to 0. */
    for (i = 2; i <= sqrt(limit); i++)
        if (prime_bool[i])
            for (j = i * i; j <= limit; j += i)
                prime_bool[j] = 0;

    /* Pass all primes out to calling array. */
    for (i = 2, j = 0; i < limit; i++)
       if (prime_bool[i])
           primes[j++] = prime_bool[i];
    primes[j] = '\0';
}

