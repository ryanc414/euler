#include <P41.h>

int main()
{
    char pandigital[NUM_DIGITS + 1];
    int len = NUM_DIGITS;

    fill_digits_reverse(pandigital, len);
    while (!is_prime(strtoul(pandigital, NULL, 10)))
        if (!permute_reverse_lexicographic(pandigital))
            fill_digits_reverse(pandigital, --len);

    printf("%s is prime.\n", pandigital);

    return 0;
}


void fill_digits_reverse(char *a, int start)
{
    int i;

    assert(start > 0);

    for (i = start; i > 0; i--)
        *a++ = i + '0';

    *a = '\0';
}

