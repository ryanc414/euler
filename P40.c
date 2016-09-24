#include <stdio.h>

#define NUM_DIGITS 7 
#define MAX_NUM_LEN sizeof(long int) * 8 + 1

void fill_digit_nums(long int *);
void fill_digit_values(char *, long int *);
char retrieve_digit(long int, long int, long int);
int number_of_digits(int);
void print_final_product(char *);


main()
{
    long int digit_nums[NUM_DIGITS];
    char digit_values[NUM_DIGITS];

    fill_digit_nums(digit_nums);
    fill_digit_values(digit_values, digit_nums);
    print_final_product(digit_values);

    return 0;
}


/* Fill an array with integer elements, starting with 1 and multiplying by 10
 * each time. */
void fill_digit_nums(long int *target_array)
{
    int i;
    long int n;

    for (i = 0, n = 1; i < NUM_DIGITS; n *= 10)
        target_array[i++] = n;
}


/* Find the value of the digit numbers (defined in digit_nums) in 
 * Champernowne's constant. */
void fill_digit_values(char *digit_values, long int *digit_nums)
{
    long int n, n_digits;     
    int i, curr_num_digits;

    for (n = 1, i = 0, n_digits = 0; i < NUM_DIGITS; n++) {
        n_digits += (curr_num_digits = number_of_digits(n));
        if (n_digits  >= digit_nums[i])
            digit_values[i++] = 
                retrieve_digit(digit_nums[i],
                                n_digits - curr_num_digits, n);
    }
}

/* Retrieve the digit at position target, for a number that starts after 
 * position start. */
char retrieve_digit(long int target, long int start, long int num)
{
    int i;
    char num_str[MAX_NUM_LEN];

    sprintf(num_str, "%ld", num);

    return num_str[target - start - 1] - '0';
}


/* Count the number of digits in an integer n. */
int number_of_digits(int n)
{
    int digit_count;

    for (digit_count = 1; n /= 10; digit_count++)
        ;

    return digit_count;
}


void print_final_product(char *digit_values)
{
    int i, final_product;
    
    for (i = 0, final_product = 1; i < NUM_DIGITS; i++)
        final_product *= digit_values[i];
    printf("Product of all target digits: %d\n", final_product);
}

