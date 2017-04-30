#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>
#include <assert.h>
#include <string.h>
#include <inttypes.h>


/* Macros for swapping elements of type t. */
#define SWAP(t, x, y) t tmp = (y); (y) = (x); (x) = tmp;
#define SWAP_ARRAY(t, a, i, j) t tmp = a[j]; a[j] = a[i]; a[i] = tmp;

/* binsearch.c */
size_t binsearch(long val, long *array, size_t lim);

/* permute.c */
bool permute_lexicographic(char *a);
bool permute_reverse_lexicographic(char *a);

/* primes.c */
bool is_prime(unsigned long n);
unsigned long *prime_sieve(unsigned long *num_primes, unsigned long limit);

/* reverse.c */
void reverse(char *s);

/* digits.c */
bool is_digit(char digit);
uint8_t num_digits(uint32_t x);
uint64_t concat_uint32(uint32_t x, uint32_t y);
bool is_pandigital(uint32_t x, uint8_t n);

