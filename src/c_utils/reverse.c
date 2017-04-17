#include <utils.h>

void swap_and_inc(char *s, int left, int right);


/* reverse(s): reverses a null-terminated character string s in place        *
 * recursively.                                                              */
void reverse(char *s)
{
    size_t len;

    for (len = 0; s[len] != '\0'; len++)
        ;
    swap_and_inc(s, 0, len - 1);
}


/* swap_and_inc(s, left, right): swaps left and right positions in s and     *
 * increments recursively inwards until s is completely reversed.            */
void swap_and_inc(char *s, int left, int right)
{
    if (left < right) {
        SWAP_ARRAY(char, s, left, right);
        swap_and_inc(s, ++left, --right);
    }
}

