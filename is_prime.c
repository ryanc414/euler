#include <math.h>

int is_prime(int n)
{
    int divisor, limit = (int) sqrt(n);
    
    for (divisor = 2; divisor <= limit; divisor++)
        if (n % divisor == 0)
            return 0;
    return 1;
}
