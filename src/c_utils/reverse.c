#include <utils.h>


/* reverse(s): reverses a character string s in place recursively. */
void reverse(char s[])
{
    int i, len;

    i = 0;
    for (len = 0; s[len] != '\0'; len++)
        ;
    swap_and_inc(s, i, len - 1);
}


/* swap_and_inc(s, left, right): swaps left and right positions in s and
 * increments recursively inwards until s is completely reversed. */
void swap_and_inc(char s[], int left, int right)
{
    if (left < right) {
        swap_elements(s, left++, right--);
        swap_and_inc(s, left, right);
    }
}


/* swap_elements: interchange v[i] and v[j] */ 
void swap_elements(char v[], int i, int j)
{
    SWAP(int, v[i], v[j]);
}

