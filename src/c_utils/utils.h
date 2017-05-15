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

/* permute.c */
bool permute_lexicographic(char *a);
bool permute_reverse_lexicographic(char *a);

/* primes.c */
bool is_prime(uint32_t n);
uint32_t *prime_sieve(uint32_t *num_primes, uint32_t limit);

/* reverse.c */
void reverse(char *s);

/* digits.c */
bool is_digit(char digit);
uint8_t num_digits(uint32_t x);
uint64_t concat_uint32(uint32_t x, uint32_t y);
bool is_pandigital(uint32_t x, uint8_t n);

/* compfuncs.c */
int comp_uint32(const void *x, const void *y);
int comp_uint64(const void *x, const void *y);
int comp_int32(const void *x, const void *y);
int comp_int64(const void *x, const void *y);

