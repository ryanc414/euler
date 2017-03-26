#include <stdio.h>

int is_prime(int n);
int prime_and_two_sq(int n);


main()
{
    int n;

    for (n = 3; prime_and_two_sq(n); n += 2)
        ;

    printf("%d violates the conjecture.\n", n);
    
    return 0;
}


int prime_and_two_sq(int n)
{
    int i, resid;

    for (i = 0; (resid = n - 2 * i * i) > 0; i++)
        if (is_prime(resid))
            return 1;
    return 0;
}

