#include <stdio.h>
#include <math.h>

#define N_INIT          1 
#define T(n)            ((n) * ((n) + 1) / 2)
#define INV_PENT(p)     ((1 + sqrt(1 + 24 * (p))) / 6)
#define INV_HEX(p)      ((1 + sqrt(1 + 8 * (h))) / 4)

int is_pentagonal(long int);
int is_hexagonal(long int);

main()
{
    long int n = N_INIT, t;

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

