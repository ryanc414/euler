#include <P40.h>

int main()
{
    uint32_t digit_nums[NUM_DIGITS];
    uint8_t digit_values[NUM_DIGITS];

    fill_digit_nums(digit_nums);
    fill_digit_values(digit_values, digit_nums);
    print_final_product(digit_values);

    return 0;
}


/* Fill an array with integer elements, starting with 1 and multiplying by 10
 * each time. */
void fill_digit_nums(uint32_t *target_array)
{
    int i;
    uint32_t n;

    for (i = 0, n = 1; i < NUM_DIGITS; n *= 10)
        target_array[i++] = n;
}


/* Find the value of the digit numbers (defined in digit_nums) in
 * Champernowne's constant. */
void fill_digit_values(uint8_t *digit_values, uint32_t *digit_nums)
{
    uint32_t n, total_digits;
    int i, next_digits;

    for (n = 1, i = 0, next_digits = 1, total_digits = 0; i < NUM_DIGITS; n++) {
        if (n == digit_nums[next_digits])
            next_digits++;
        total_digits += next_digits;
        if (total_digits  >= digit_nums[i]) {
            digit_values[i] =
                retrieve_digit(digit_nums[i], total_digits - next_digits, n);
            i++;
        }
    }
}

/* Retrieve the digit at position target, for a number that starts after
 * position start. */
uint8_t retrieve_digit(uint32_t target, uint32_t start, uint32_t num)
{
    char num_str[MAX_NUM_LEN];

    sprintf(num_str, "%" PRIu32, num);

    return (uint8_t) (num_str[target - start - 1] - '0');
}


void print_final_product(uint8_t *digit_values)
{
    uint32_t i, final_product;

    for (i = 0, final_product = 1; i < NUM_DIGITS; i++)
        final_product *= digit_values[i];
    printf("Product of all target digits: %" PRIu32 "\n", final_product);
}

