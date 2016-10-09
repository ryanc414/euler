#include <stdio.h>

#define NUM_DIGITS 9

void fill_digits_reverse(char *, int);
void permute(char *, int *);
int find_next_k(char *, int);
int find_next_l(char *, int, int);
int is_prime(int);
void reverse(char *);


main()
{
    char pandigital[NUM_DIGITS + 1];
    int len = NUM_DIGITS;

    fill_digits_reverse(pandigital, len);
    while (!is_prime(atoi(pandigital)))
        permute(pandigital, &len);

    printf("%s is prime.\n", pandigital);

    return 0;
}


void fill_digits_reverse(char *a, int start)
{
    int i;

    for (i = start; i > 0; i--)
        *a++ = i + '0';

    *a = '\0';
}


/* Permutes a character array a in reverse lexicographic order. The array must
 * be null-terminated. */
void permute(char *a, int *len)
{
    int k, l;
   
    k = find_next_k(a, *len);
    if (k < 0)
        fill_digits_reverse(a, --*len);
    else {
        l = find_next_l(a, *len, k);
        swap_elements(a, k, l);
        reverse(a + k + 1);
    }
}


int find_next_k(char *a, int len)
{
    int k;

    for (k = len - 2; k >= 0; k--)
        if (a[k] > a[k + 1])
            return k;
    return -1;
}


int find_next_l(char *a, int len, int k)
{
    int l;

    for (l = len - 1; l >= 0; l--)
        if (a[k] > a[l])
            return l;
    return -1;
}

