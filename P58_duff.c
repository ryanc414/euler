#include <stdio.h>

#define STEP_SIZE 2
#define NUM_STEPS 4
#define TARGET 10
#define ABOVE_RATIO(PRIMES, TOTAL) (PRIMES) * TARGET >= (TOTAL)
#define DO_STEP                                                               \
        n += step;                                                            \
        if (is_prime(n))                                                      \
            prime_count++;                                                    \
        total_count++

int is_prime(int);
int find_side_length(void);

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
    n = 43;
    step = 6;
    prime_count = 8;
    total_count = 12;

    /* Now iterate through the sequence. */
    switch ((total_count - 1) % NUM_STEPS) {
    case 0: do {step += STEP_SIZE;
                DO_STEP;
    case 1:     DO_STEP;
    case 2:     DO_STEP;
    case 3:     DO_STEP;
            } while (ABOVE_RATIO(prime_count, total_count));
    }

    return step + 1;  /* Side length is one greater than the step size. */
}

