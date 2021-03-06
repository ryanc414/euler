#include <problems.h>

#define SUBSTR_LEN 3
#define NUM_DIVISORS 7
#define PANDIGITAL_LEN 10
#define SUBSTR_NO_DIVISOR(substr, divisor) \
    (atoin((substr), (SUBSTR_LEN)) % (divisor))

bool substring_divisors(char *);
uint32_t atoin(char *, uint8_t);

static const char divisors[] = {2, 3, 5, 7, 11, 13, 17};
static const char starting_digits[] = {1, 2, 3, 4, 5, 6, 7};

