/* Header file for P58.c */

#include <problems.h>

#define STEP_SIZE 2
#define NUM_STEPS 4
#define TARGET 10
#define ABOVE_RATIO(PRIMES, TOTAL) (PRIMES) * TARGET >= (TOTAL)

int find_side_length(void);

