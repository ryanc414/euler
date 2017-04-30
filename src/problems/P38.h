/* Header file for P38.c */

#include <problems.h>

/* Function prototypes for P38.c */
uint32_t find_largest_pandigital(void);
uint32_t find_concatenated_product(uint32_t x);

/* Limits for 9-digit numbers - LOWER_LIMIT <= x < UPPER_LIMIT. */
#define UPPER_LIMIT 1000000000L
#define LOWER_LIMIT 100000000L

/* Upper limit for x. Since n > 1 x cannot be longer than 4 digits. */
#define UPPER_X_LIMIT 10000

/* We are looking for 1 to 9 pandigitals. */
#define PANDIGITAL_SIZE 9

