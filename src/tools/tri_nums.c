#include <stdio.h>

#define T(n) n * (n + 1) / 2


main()
{
    int t, n = 1;

    while ((t = T(n++)) <= 196)
        ;

    printf("%dth tri-num is %d", n, t);

    return 0;
}

