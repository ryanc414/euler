#include <utils.h>


/* is_prime(n): check if integer n is prime, by looking for divisors. */
bool is_prime(unsigned long n)
{
    long divisor, limit = (long) sqrt(n);

    for (divisor = 2; divisor <= limit; divisor++)
        if (n % divisor == 0)
            return 0;
    return n > 1; /* 1 is not prime! */
}


/* prime_sieve(): Uses a Sieve of Eratosthenes to find all primes below      *
 * limit. Allocates enough memory to store the primes - it is the caller's   *
 * responsibility to free this memory. Returns the number of primes found.   */
unsigned long *prime_sieve(unsigned long *num_primes, unsigned long limit)
{
    unsigned long i, j;
    unsigned long sqrt_limit = (unsigned long) sqrt(limit);
    unsigned long *primes = NULL;
    bool prime_bool[limit];

    /* Initialise the bool array. */
    for (i = 2; i < limit; i++)
        prime_bool[i] = true;

    /* Set each non-prime to false. */
    for (i = 2; i <= sqrt_limit; i++)
        if (prime_bool[i])
            for (j = i * i; j <= limit; j += i)
                prime_bool[j] = false;

    /* Count the number of  primes. */
    *num_primes = 0;
    for (i = 2; i < limit; i++)
        if (prime_bool[i])
            (*num_primes)++;

    /* Allocate memory for the primes. */
    primes = malloc((*num_primes) * sizeof(unsigned long));
    assert(primes != NULL);

    /* Add all primes out to output array. */
    for (i = 2, j = 0; i < limit; i++)
       if (prime_bool[i])
           primes[j++] = i;

    return primes;
}

