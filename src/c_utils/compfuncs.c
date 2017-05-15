/* Provides comparison functions between various types. */

#include <utils.h>

/* comp_*(x, y): returns the difference x - y for each type. */
int comp_uint32(const void *x, const void *y)
{
    return *(uint32_t *)x - *(uint32_t *)y;
}

int comp_uint64(const void *x, const void *y)
{
    return *(uint64_t *)x - *(uint64_t *)y;
}

int comp_int32(const void *x, const void *y)
{
    return *(int32_t *)x - *(int32_t *)y;
}

int comp_int64(const void *x, const void *y)
{
    return *(int64_t *)x - *(int64_t *)y;
}

