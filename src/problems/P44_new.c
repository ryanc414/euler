#include <stdio.h>

#define P(n) ((n) * (3 * (n) - 1) / 2)
#define CACHE_SIZE 10000

void fill_p_cache(void);
int is_pentagonal(long int);
long int binsearch(size_t, long int *, size_t);

long int p_cache[CACHE_SIZE];


main()
{
    long int i, j;

    fill_p_cache();

    for (i = 2; i < CACHE_SIZE; i++)
        for (j = 1; j < i; j++)
            if (is_pentagonal(p_cache[i] + p_cache[j]) &&
                is_pentagonal(p_cache[i] - p_cache[j])) {
                printf("Smallest D is %ld\n", p_cache[i] - p_cache[j]);
                return 0;
            }

    return 1;
}


void fill_p_cache(void)
{
    int n;

    for (n = 1; n <= CACHE_SIZE; n++)
        p_cache[n - 1] = P(n);
}


/* is_pentagonal: checks if a given number is pentagonal. */
int is_pentagonal(long int test)
{
    return binsearch(test, p_cache, CACHE_SIZE) >= 0;
}

