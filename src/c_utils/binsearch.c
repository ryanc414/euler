#include <utils.h>

int binsearch(int val, int *array, int lim)
{
    unsigned int low, high, mid;

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

