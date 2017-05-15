/* P8 - largest product of adjacent digits. */

#include <P8.h>

/* Find the largest product of ADJ_DIGITS adjacent digits in the specified
 * input file. */
int main(int argc, char *argv[])
{
    uint64_t largest_product;

    if (read_input_num(argc, argv) != 0)
        return 1;

    largest_product = find_largest_product();

    printf("Largest product of %u adjacent digits is %" PRIu64 ".\n",
            ADJ_DIGITS,
            largest_product);

    return 0;
}


/* Read the digits in the input file into the bignum array, ignoring any      *
 * non-digit characters such as whitespace.                                   */
int read_input_num(int argc, char *argv[])
{
    FILE *fp;
    int i = 0;
    char next_char;

    if (argc < 2) {
        printf("Usage: ./P8 [input filename]\n");
        return 1;
    }

    fp = fopen(argv[1], "r");

    if (fp == NULL) {
        printf("Error, could not open filename specified: %s\n.", argv[1]);
        return 2;
    }

    while (i < NUMSIZE) {
        next_char = fgetc(fp);
        if (is_digit(next_char))
            bignum[i++] = next_char - '0';
    }

    return 0;
}


/* Finds the largest product of successive digits in the bignum array. */
uint64_t find_largest_product(void)
{
    uint64_t product;
    uint64_t max_product = 0;
    int i;

    for (i = 0; i + ADJ_DIGITS < NUMSIZE; i++) {
        product = find_product(i);
        if (product > max_product)
            max_product = product;
    }

    return max_product;
}


/* Find the product of the first ADJ_DIGITS digits in the bignum array. */
uint64_t find_product(int i)
{
    uint64_t product;
    int j;

    for (j = 0, product = 1; j < ADJ_DIGITS; j++)
        product *= (uint64_t) bignum[i + j];

    return product;
}

