/* P38 - Pandigital multiples
 *
 * Find the largest 1 to 9 pandigital number that is formed by concatenating
 * the products of an integer with integers 1 to n with n > 1.
 */

#include <P38.h>


int main(void)
{
    printf("Largest 1 to 9 pandigital formed is: %" PRIu32 "\n",
            find_largest_pandigital());

    return 0;
}

/* Find the largest 1 to 9 pandigital that can be formed from any x and
 * (1...n).
 */
uint32_t find_largest_pandigital(void)
{
    uint32_t x;
    uint32_t next_pandigital;
    uint32_t largest_pandigital = 0;

    for (x = 1; x < UPPER_X_LIMIT; x++) {
        if ((next_pandigital = find_concatenated_product(x))
                > largest_pandigital) {
            largest_pandigital = next_pandigital;
        }
    }

    return largest_pandigital;
}


/* Find the largest 1 to 9 pandigital product that can be formed from a
 * particular value of x and any (1...n). Returns the largest valid product or
 * 0 if none is found.
 */
uint32_t find_concatenated_product(uint32_t x)
{
    uint32_t i;
    uint64_t concat_product = 0;
    uint64_t largest_concat_product = 0;

    for (i = 1;
         (concat_product = concat_uint32(concat_product, x * i)) < UPPER_LIMIT;
         i++) {
        if (concat_product >= LOWER_LIMIT
                && is_pandigital(concat_product, PANDIGITAL_SIZE)) {
            largest_concat_product = concat_product;
        }
    }

    return (uint32_t) largest_concat_product;
}

