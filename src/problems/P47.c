#include <stdio.h>
#include <math.h>

#define NUM_FACTORS 4 
#define LIMIT 1000000l

int num_distinct_prime_factors(long int);
void prime_sieve(long int *primes, long int limit);
long int primes[LIMIT];

int main()
{
    long int n;
    int count = 0;

    prime_sieve(primes, LIMIT);

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
