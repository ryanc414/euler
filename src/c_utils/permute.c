#include <utils.h>

/* Prototypes for private functions used by this module. */
bool less_than(size_t x, size_t y);
bool greater_than(size_t x, size_t y);
bool permute(char *a, bool (*comp)(size_t, size_t));
size_t find_next_k(char *a, size_t len, bool (*comp)(size_t, size_t));
size_t find_next_l(char *a, size_t len, size_t k, bool (*comp)(size_t, size_t));


/* Permutes a character array a in lexicographic order. The array must be    *
 * null-terminated. Returns 0 if no more permutations exist.                 */
bool permute_lexicographic(char *a)
{
    return permute(a, less_than);
}


/* Permutes a character array a in lexicographic order. The array must be
 * null-terminated. Returns 0 if no more permutations exist. */
bool permute_reverse_lexicographic(char *a)
{
    return permute(a, greater_than);
}


/* Compare x < y. */
bool less_than(size_t x, size_t y)
{
    return x < y;
}


/* Compare x > y. */
bool greater_than(size_t x, size_t y)
{
    return x > y;
}


/* Permutes a character array a in an order defined by the comparison        *
 * function provided. Returns false if no more permutations can be found.    */
bool permute(char *a, bool (*comp)(size_t, size_t))
{
    size_t k, l;
    size_t len = strlen(a);

    k = find_next_k(a, len, comp);
    if (k == len)
        return false;
    else {
        l = find_next_l(a, len, k, comp);
        SWAP_ARRAY(char, a, k, l);
        reverse(a + k + 1);
    }
    return true;
}


/* Find the next k value to use in the permutation algorithm, sorting        *
 * according to the comp function provided.                                  */
size_t find_next_k(char *a, size_t len, bool (*comp)(size_t, size_t))
{
    size_t k;

    /* k will underflow at 0 so check that it is less than len to avoid a    *
     * segfault.                                                             */
    for (k = len - 2; k < len; k--)
        if (comp(a[k], a[k + 1]))
            return k;
    return len;
}


/* Find the next l value to use in the permutation algorithm, sorting        *
 * according to the comp function provided.                                  */
size_t find_next_l(char *a, size_t len, size_t k, bool (*comp)(size_t, size_t))
{
    size_t l;

    for (l = len - 1; l < len; l--)
        if (comp(a[k], a[l]))
            return l;

    assert(false);
}

