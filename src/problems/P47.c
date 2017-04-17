#include <P47.h>


int main()
{
    long int n;
    int count = 0;
    unsigned long num_primes;

    primes = prime_sieve(&num_primes, LIMIT);

    for (n = 2; count != NUM_FACTORS; n++)
        if (num_distinct_prime_factors(n) != NUM_FACTORS)
            count = 0;
        else
            ++count;

    printf("First number is: %ld\n", n - NUM_FACTORS);

    return 0;
}


int num_distinct_prime_factors(long int n)
{
    long int i;
    int count = 0;

    for (i = 0; primes[i] <= n; i++)
        if (n % primes[i] == 0)
            count++;

    return count;
}
