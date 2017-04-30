#include <P44.h>


int main()
{
    long i, j;

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
    long n;

    for (n = 1; n <= CACHE_SIZE; n++)
        p_cache[n - 1] = P(n);
}


/* is_pentagonal: checks if a given number is pentagonal. */
bool is_pentagonal(long test)
{
    return binsearch(test, p_cache, CACHE_SIZE) != CACHE_SIZE;
}

