#include <stdio.h>

long int binsearch(size_t val, long int *array, size_t lim)
{
    unsigned long int low, high, mid;

    low = 0;
    high = lim - 1;
    while (low < high) {
        mid = (low + high) / 2;
        if (val > array[mid])
            low = mid + 1;
        else
            high = mid;
    }
    if (array[low] == val)
        return low;
    else
        return -1;  /* no match */
}

