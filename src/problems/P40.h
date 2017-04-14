#include <problems.h>

#define NUM_DIGITS 7
#define MAX_NUM_LEN sizeof(long int) * 8 + 1

void fill_digit_nums(long int *);
void fill_digit_values(char *, long int *);
char retrieve_digit(long int, long int, long int);
int number_of_digits(int);
void print_final_product(char *);

