#include <P44.h>


int main()
{
    long n;

    fill_p_cache();

    for (n = 1; !is_smallest_difference(n); n++)
        printf("Testing D = %ld\n", p_cache[n]);

    printf("Smallest D is %ld\n", P(n));

    return 0;
}


void fill_p_cache(void)
{
    long n;

    for (n = 1; n <= CACHE_SIZE; n++)
        p_cache[n - 1] = P(n);
}


/* is_smallest_difference: given the nth pentagonal number, find a pair of
 * pentagonal numbers which subtract to give it. If a pair is found, check
 * if the pair also sums to give a pentagonal number. */
bool is_smallest_difference(long n)
{
    long i, j, lower, upper, difference, target;
    target = p_cache[n];
    j = n + 1;
    upper = p_cache[j];

    for (i = 1; i < j; i++) {
        lower = p_cache[i];
        if ((difference = upper - lower) == target) {
            if (is_pentagonal(upper + lower))
                return true;
            else
                reset_to_next_upper(&i, &j, &upper);
        } else if (difference < target)
            reset_to_next_upper(&i, &j, &upper);
    }

    /* If we've got this far no pairs exist. */
    return false;
}


/* is_pentagonal: checks if a given number is pentagonal. */
bool is_pentagonal(long test)
{
    return binsearch(test, p_cache, CACHE_SIZE) != CACHE_SIZE;
}


/* reset_to_next_upper: reset the upper and lower parameters to continue
 * checking possible pentagonal pairs. */
void reset_to_next_upper(long *i, long *j, long *upper)
{
    *i = 0;
    (*j)++;
    *upper = p_cache[*j];
}

