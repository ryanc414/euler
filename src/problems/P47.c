#include <P47.h>


int main()
{
    uint32_t n;
    uint32_t num_primes;
    uint8_t count = 0;

    primes = prime_sieve(&num_primes, LIMIT);

    for (n = 2; count != NUM_FACTORS; n++)
        if (num_distinct_prime_factors(n) != NUM_FACTORS)
            count = 0;
        else
            ++count;

    printf("First number is: %" PRIu32 "\n", n - NUM_FACTORS);

    return 0;
}


uint8_t num_distinct_prime_factors(uint32_t n)
{
    uint32_t i;
    uint8_t count = 0;

    for (i = 0; primes[i] <= n; i++)
        if (n % primes[i] == 0)
            count++;

    return count;
}

