#include <utils.h>

size_t binsearch(long val, long *array, size_t lim)
{
    size_t low, high, mid;

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
        return lim;  /* no match */
}

