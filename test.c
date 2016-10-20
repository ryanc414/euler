#include <stdio.h>
#define LIMIT 10 

static int a[LIMIT];
void prime_sieve(int *primes, int limit);

main()
{
    int i;
    prime_sieve(a, LIMIT);

    for (i = 0; a[i] != '\0'; i++)
        printf("%d ", a[i]);

    return 0;
}

