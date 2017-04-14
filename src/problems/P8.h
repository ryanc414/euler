/* Header file for P8.c */

#include <problems.h>

/* We know that the input contains 1000 digits so hardcode this here. */
#define NUMSIZE 1000
#define ADJ_DIGITS 13

/* Array for holding the digits. */
static char bignum[NUMSIZE];

/* P8.c functions */
int read_input_num(int argc, char *argv[]);
long long unsigned int find_largest_product(void);
long long unsigned int find_product(int i);

