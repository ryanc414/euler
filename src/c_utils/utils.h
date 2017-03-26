#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define SWAP(t, x, y) t tmp = (y); (y) = (x); (x) = tmp;

/* binsearch.c */
int binsearch(int, int *, int);

/* heap.c */
void generate(int, char *);
void swap(char *, int, int);
void print_array(char *A);

/* permute.c */
int permute(char *, int);
int find_next_k(char *, int);
int find_next_l(char *, int, int);
void swap_elements(char *, int, int);

/* primes.c */
int is_prime(int);
int prime_sieve(int **, int);

/* reverse.c */
void reverse(char *);
void swap_and_inc(char *, int, int);
void swap_elements(char *, int, int);

/* permute.c */
int permute(char *, int);
int find_next_k(char *, int);
int find_next_l(char *, int, int);
