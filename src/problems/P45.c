#include <P45.h>


int main()
{
    uint64_t n, t;

    n = N_INIT;

    while (!(is_pentagonal(t = T(n)) && is_hexagonal(t)))
        n++;

    printf("%" PRIu64 " is triangular, pentagonal and hexagonal.\n", t);

    return 0;
}


/* An integer is pentagonal if 1 + sqrt(1 + 24P) is a multiple of 6. */
bool is_pentagonal(uint64_t p)
{
    double m = INV_PENT(p);
    return m == floor(m);
}


/* An integer is hexagonal if 1 + sqrt(1 + 8H) is a multiple of 4. */
bool is_hexagonal(uint64_t h)
{
    double m = INV_HEX(p);
    return m == floor(m);
}

