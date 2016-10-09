#include <stdio.h>

#define P(n) ((n) * (3 * (n) - 1) / 2)
#define CACHE_SIZE 1000000

void fill_p_cache(void);
int is_smallest_difference(long int);
int is_pentagonal(long int);
void reset_to_next_upper(long int *, long int *, long int *);
long int binsearch(size_t, long int *, size_t);

long int p_cache[CACHE_SIZE];

main()
{
    long int n;

    fill_p_cache();

    for (n = 1; !is_smallest_difference(n); n++)
        printf("Testing D = %ld\n", p_cache[n]);

    printf("Smallest D is %ld\n", P(n));

    return 0;
}


void fill_p_cache(void)
{
    int n;

    for (n = 1; n <= CACHE_SIZE; n++)
        p_cache[n - 1] = P(n);
}


/* is_smallest_difference: given the nth pentagonal number, find a pair of
 * pentagonal numbers which subtract to give it. If a pair is found, check
 * if the pair also sums to give a pentagonal number. */
int is_smallest_difference(long int n)
{
    long int i, j, lower, upper, difference, target;
    target = p_cache[n];
    j = n + 1;
    upper = p_cache[j];

    for (i = 1; i < j; i++) {
        lower = p_cache[i];
        if ((difference = upper - lower) == target) {
            if (is_pentagonal(upper + lower))
                return 1;
            else
                reset_to_next_upper(&i, &j, &upper);
        } else if (difference < target)
            reset_to_next_upper(&i, &j, &upper);
    }

    /* If we've got this far no pairs exist. */
    return 0;
}


/* is_pentagonal: checks if a given number is pentagonal. */
int is_pentagonal(long int test)
{
    return binsearch(test, p_cache, CACHE_SIZE) >= 0;
}

/* reset_to_next_upper: reset the upper and lower parameters to continue
 * checking possible pentagonal pairs. */
void reset_to_next_upper(long int *i, long int *j, long int *upper)
{
    *i = 0;
    (*j)++;
    *upper = p_cache[*j];
}

