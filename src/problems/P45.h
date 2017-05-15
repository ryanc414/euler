/* Header file for P45.c */

#include <problems.h>

#define N_INIT          286
#define T(n)            ((n) * ((n) + 1) / 2)
#define INV_PENT(p)     ((1 + sqrt(1 + 24 * (p))) / 6)
#define INV_HEX(p)      ((1 + sqrt(1 + 8 * (h))) / 4)

bool is_pentagonal(uint64_t);
bool is_hexagonal(uint64_t);

