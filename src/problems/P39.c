/* P39 - Find value p = a + b + c where a^2 + b^2 = c^2 with most integral
 * solutions for p <= 1000.
 */

#include <P39.h>


/* Find the number of solutions for each value of 1 <= p <= 1000. At the end,
 * print the value of p with the maximum number of solutions.
 */
int main(void)
{
    uint16_t p_solutions[P_LIMIT];

    memset(p_solutions, 0x00, P_LIMIT * sizeof(uint16_t));
    find_solutions(p_solutions);
    printf("Max solutions for p = %" PRIu16 "\n", find_max_p_solutions(p_solutions));

    return 0;
}


/* Find solutions for p and store the number found in an array passed in. */
void find_solutions(uint16_t *p_solutions)
{
    uint16_t a, b, c, p;

    for (a = 1; a < SIDE_LIMIT; a++)
        for (b = a; b < SIDE_LIMIT; b++)
            if ((c = find_c(a, b)) != 0)
                if ((p = a + b + c) <= P_LIMIT)
                    p_solutions[p - 1]++;
}


/* Find the value of p with the most solutions. */
uint16_t find_max_p_solutions(uint16_t *p_solutions)
{
    uint16_t p;
    uint16_t max_sol = 0;
    uint16_t max_sol_p = 0;

    for (p = 1; p <= P_LIMIT; p++) {
        if (p_solutions[p - 1] > max_sol) {
            max_sol = p_solutions[p - 1];
            max_sol_p = p;
        }
    }

    return max_sol_p;
}


/* Finds c where a^2 + b^2 = c^2. Returns 0 if no integral c exists. */
uint16_t find_c(uint16_t a, uint16_t b)
{
    uint32_t c_sq = a * a + b * b;
    double c = sqrt(c_sq);

    if (c == floor(c))
        return (uint16_t) c;
    return 0;
}

