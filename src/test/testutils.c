/* Tests for libutils.so */

#include <utils.h>

/* Prototypes for test functions. */
int test_binsearch(void);
int test_permute_lexicographic(void);
int test_permute_reverse_lexicographic(void);
int test_reverse(void);
int test_is_prime(void);
int test_prime_sieve(void);
int test_is_digit(void);


/* Run all tests for the utils library. */
int main(void)
{
    test_binsearch();
    test_permute_lexicographic();
    test_permute_reverse_lexicographic();
    test_reverse();
    test_is_prime();
    test_prime_sieve();
    test_is_digit();

    printf("\nAll tests passed\n\n");
    return 0;
}


/* Test the binsearch function. */
int test_binsearch(void)
{
    size_t len = 5;
    long test_arr[len];
    size_t i;

    /* Fill the test array with values corresponding to indices. */
    for (i = 0; i < len; i++)
        test_arr[i] = i;

    /* Check that we can find all values in the test array. */
    for (i = 0; i < len; i++)
        assert(binsearch(i, test_arr, len) == i);

    /* Test that searching for a value not in the array returns the length   *
     * of the array to signify the value could not be found. */
    assert(binsearch(len, test_arr, len) == len);

    printf("test_binsearch passed\n");

    return 0;
}


/* Test the permute_lexicographic function. */
int test_permute_lexicographic(void)
{
    char test_arr[] = "abcde";

    /* Permute the array until completely reversed. */
    while (permute_lexicographic(test_arr))
        ;

    /* Check that the array is now reversed. */
    assert(!strcmp(test_arr, "edcba"));

    printf("test_permute_lexicographic passed\n");

    return 0;
}


/* Test the permute_reverse_lexicographic function. */
int test_permute_reverse_lexicographic(void)
{
    char test_arr[] = "edcba";

    /* Permute the array until completely reversed. */
    while (permute_reverse_lexicographic(test_arr))
        ;

    /* Check that the array is now reversed. */
    assert(!strcmp(test_arr, "abcde"));

    printf("test_permute_reverse_lexicographic passed\n");

    return 0;
}


/* Test the reverse function. */
int test_reverse(void)
{
    char test_str[] = "Hello, world.";

    /* Test that the entire string can be revered. */
    reverse(test_str);
    assert(!strcmp(test_str, ".dlrow ,olleH"));

    /* Test that a substring can be reversed. */
    reverse(test_str + 7);
    assert(!strcmp(test_str, ".dlrow Hello,"));

    printf("test_reverse passed\n");

    return 0;
}


/* Test the is_prime function. */
int test_is_prime(void)
{
    /* Test the numbers 0-5 are all correct. */
    assert(!is_prime(0));
    assert(!is_prime(1));
    assert(is_prime(2));
    assert(is_prime(3));
    assert(!is_prime(4));
    assert(is_prime(5));

    /* Check a couple of larger numbers. */
    assert(!is_prime(49));
    assert(is_prime(97));

    printf("test_is_prime passed\n");

    return 0;
}


/* Test the prime_sieve function. */
int test_prime_sieve(void)
{
    unsigned long num_primes = 0;
    unsigned long limit = 10;
    unsigned long expct_primes[] = {2, 3, 5, 7};
    unsigned long expct_num_primes = 4;
    int i;

    /* Use the sieve to find primes. */
    unsigned long *primes = prime_sieve(&num_primes, limit);

    /* Check that the expected primes are returned. */
    assert(num_primes == expct_num_primes);
    for (i = 0; i < num_primes; i++)
        assert(primes[i] == expct_primes[i]);

    printf("test_prime_sieve passed\n");

    return 0;
}


/* Test the is_digit function. */
int test_is_digit(void)
{
    char c;

    for (c = '0'; c <= '9'; c++)
        assert(is_digit(c));
    assert(!is_digit(c));
    assert(!is_digit('0' - 1));
    assert(!is_digit('\0'));
    assert(!is_digit('m'));

    printf("test_is_digit passed.\n");

    return 0;
}
