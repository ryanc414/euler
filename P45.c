#include <stdio.h>

#define CACHE_SIZE 1000000
#define T_START 286
#define T(n) ((n) * ((n) + 1) / 2)
#define P(n) ((n) * (3 * (n) - 1) / 2)
#define H(n) ((n) * (2 * (n) - 1))
#define IS_PENTAGONAL(n) (binsearch(n, p_cache, CACHE_SIZE) >= 0)
#define IS_HEXAGONAL(n) (binsearch(n, h_cache, CACHE_SIZE) >= 0)


long int binsearch(size_t, long int *, size_t);
void fill_caches(void);

static long int t_cache[CACHE_SIZE];
static long int p_cache[CACHE_SIZE];
static long int h_cache[CACHE_SIZE];


main()
{
    int n;

    fill_caches();

    for (n = T_START; n <= CACHE_SIZE; n++)
        if (IS_PENTAGONAL(t_cache[n]) && IS_HEXAGONAL(t_cache[n])) {
            printf("%ld is triangular, pentagonal and hexagonal.\n", t_cache[n]);
            return 0;
        }

    return 1;
}


void fill_caches(void)
{
    int n;

    for (n = 1; n <= CACHE_SIZE; n++) {
        t_cache[n] = T(n);
        p_cache[n] = P(n);
        h_cache[n] = H(n);
    }
}

