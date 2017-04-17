#include <problems.h>

#define P(n) ((n) * (3 * (n) - 1) / 2)
#define CACHE_SIZE 10000

void fill_p_cache(void);
bool is_pentagonal(long);

long p_cache[CACHE_SIZE];
