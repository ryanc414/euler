#include <problems.h>

#define NUM_DIGITS 7
#define MAX_NUM_LEN sizeof(uint32_t) * 8 + 1

void fill_digit_nums(uint32_t *);
void fill_digit_values(uint8_t *, uint32_t *);
uint8_t retrieve_digit(uint32_t, uint32_t, uint32_t);
int number_of_digits(int);
void print_final_product(uint8_t *);

