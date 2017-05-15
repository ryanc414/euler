#include <P46.h>


int main()
{
    uint32_t n;

    for (n = 3; prime_and_two_sq(n); n += 2)
        ;

    printf("%" PRIu32 " violates the conjecture.\n", n);

    return 0;
}


bool prime_and_two_sq(uint32_t n)
{
    uint32_t i;
    int32_t resid;

    for (i = 0; (resid = n - 2 * i * i) > 0; i++)
        if (is_prime(resid))
            return true;
    return false;
}

