/* Utility functions relating to digits. */

#include <utils.h>


/* Checks if a character is a digit. */
bool is_digit(char c)
{
   return c >= '0' && c <= '9';
}


/* Count the number of digits in an integer. */
uint8_t num_digits(uint32_t x)
{
    uint8_t digit_count = 0;

    while (x) {
        digit_count++;
        x /= 10;
    }

    return digit_count;
}


/* Concatenate two uint32s.
 * e.g. x = 12, y = 34 returns 1234.
 */
uint64_t concat_uint32(uint32_t x, uint32_t y)
{
    uint64_t base = (uint64_t) x * (uint64_t) pow(10, num_digits(y));
    return base + (uint64_t) y;
}


/* Check if a number is 1 to n pandigital. */
bool is_pandigital(uint32_t x, uint8_t n)
{
    char digits[n];
    uint8_t found_digits[n + 1];
    uint8_t i;

    /* Sanity check that n is between 1 and 9 inclusive. */
    assert(n > 0 && n < 10);

    /* Convert x to an array of digit chars. Check that the correct number
     * of digits are written. */
    if (snprintf(digits, n + 1, "%" PRIu32, x) != n)
        return false;

    /* Look for any repeats. If none are found, then x is pandigital. */
    memset(found_digits, 0x00, n + 1);
    for (i = 0; i < n; i++) {
        if (digits[i] == '0' || found_digits[digits[i] - '0'])
            return false;
        found_digits[digits[i] - '0'] = 1;
    }

    return true;
}

