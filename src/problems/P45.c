#include <P45.h>


int main()
{
    long int n, t;

    n = N_INIT;

    while (!(is_pentagonal(t = T(n)) && is_hexagonal(t)))
        n++;

    printf("%ld is triangular, pentagonal and hexagonal.\n", t);

    return 0;
}


/* An integer is pentagonal if 1 + sqrt(1 + 24P) is a multiple of 6. */
int is_pentagonal(long int p)
{
    double m = INV_PENT(p);
    return m == floor(m);
}


/* An integer is hexagonal if 1 + sqrt(1 + 8H) is a multiple of 4. */
int is_hexagonal(long int h)
{
    double m = INV_HEX(p);
    return m == floor(m);
}

