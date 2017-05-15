#include <P43.h>


int main()
{
    char pandigital[] = "0123456789";
    uint64_t pandigital_sum = 0;

    do
        if (substring_divisors(pandigital))
            pandigital_sum += atoin(pandigital, PANDIGITAL_LEN);
    while (permute_lexicographic(pandigital));

    printf("The sum of pandigitals that meet the criteria is %" PRIu64 "\n",
            pandigital_sum);

    return 0;
}


/* substring_divisors: returns 1 if all the substrings of the input have the
 * required diviors, 0 otherwise. */
bool substring_divisors(char *pandigital)
{
    uint8_t i;

    for (i = 0; i < NUM_DIVISORS; i++)
        if (SUBSTR_NO_DIVISOR(pandigital + starting_digits[i], divisors[i]))
            return false;
    return true;
}


/* atoin: transform char array to integer of fixed length. */
uint32_t atoin(char *a, uint8_t n)
{
    uint8_t i;
    uint32_t result = 0;

    for (i = 0; i < n; i++)
        result = result * 10 + (a[i] - '0');
    return result;
}

