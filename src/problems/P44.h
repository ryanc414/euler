#include <problems.h>

#define P(n) ((n) * (3 * (n) - 1) / 2)
#define CACHE_SIZE 1000000

void fill_p_cache(void);
bool is_smallest_difference(long);
bool is_pentagonal(long);
void reset_to_next_upper(long *, long *, long *);

long p_cache[CACHE_SIZE];

