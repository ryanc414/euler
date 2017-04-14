#include <P58.h>


int main()
{
    printf("Side length: %d\n", find_side_length());
    return 0;
}

/* Find the side length when fewer than 10% of diagonal values are primes. */
int find_side_length(void)
{
    int i, n, step, prime_count, total_count;

    /* Define sequence start point. */
    n = 1;
    step = 0;
    prime_count = 0;
    total_count = 1;

    /* Now iterate through the sequence. */
    do {
        step += STEP_SIZE;
        for (i = 0; i < NUM_STEPS; i++) {
            n += step;
            if (is_prime(n))
                prime_count++;
            total_count++;
        }
    } while (ABOVE_RATIO(prime_count, total_count));

    return step + 1;  /* Side length is one greater than the step size. */
}

