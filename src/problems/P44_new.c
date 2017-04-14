#include <P44_new.h>


int main()
{
    int i, j;

    fill_p_cache();

    for (i = 2; i < CACHE_SIZE; i++)
        for (j = 1; j < i; j++)
            if (is_pentagonal(p_cache[i] + p_cache[j]) &&
                is_pentagonal(p_cache[i] - p_cache[j])) {
                printf("Smallest D is %d\n", p_cache[i] - p_cache[j]);
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
int is_pentagonal(int test)
{
    return binsearch(test, p_cache, CACHE_SIZE) >= 0;
}

