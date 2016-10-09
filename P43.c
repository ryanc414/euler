#include <stdio.h>

#define SUBSTR_LEN 3
#define NUM_DIVISORS 7
#define PANDIGITAL_LEN 10
#define SUBSTR_NO_DIVISOR(substr, divisor) \
    (atoin((substr), (SUBSTR_LEN)) % (divisor))

int permute(char *, int);
int substring_divisors(char *);
long int atoin(char *, int);

static const char divisors[] = {2, 3, 5, 7, 11, 13, 17};
static const char starting_digits[] = {1, 2, 3, 4, 5, 6, 7};

main()
{
    char pandigital[] = "0123456789";
    long int pandigital_sum = 0;

    do
        if (substring_divisors(pandigital))
            pandigital_sum += atoin(pandigital, PANDIGITAL_LEN);
    while (permute(pandigital, PANDIGITAL_LEN));

    printf("The sum of pandigitals that meet the criteria is %ld.\n", pandigital_sum);

    return 0;
}


/* substring_divisors: returns 1 if all the substrings of the input have the
 * required diviors, 0 otherwise. */
int substring_divisors(char *pandigital)
{
    int i;

    for (i = 0; i < NUM_DIVISORS; i++)
        if (SUBSTR_NO_DIVISOR(pandigital + starting_digits[i], divisors[i]))
            return 0;
    return 1;
}


/* atoin: transform char array to integer of fixed length. */
long int atoin(char *a, int n)
{
    int i; 
    long int result = 0;

    for (i = 0; i < n; i++)
        result = result * 10 + (a[i] - '0');
    return result;
}

