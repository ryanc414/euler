#include <problems.h>

#define P(n) ((n) * (3 * (n) - 1) / 2)
#define CACHE_SIZE 1000000

void fill_p_cache(void);
int is_smallest_difference(int);
int is_pentagonal(int);
void reset_to_next_upper(int *, int *, int *);

int p_cache[CACHE_SIZE];

