#include <problems.h>

#define T(n) n * (n + 1) / 2
#define N_LIMIT 23
#define NUM_WORDS 2000
#define MAX_WORD 15

void fill_tri_nums(void);
bool read_words(char **words, char *filename);
uint32_t count_tri_nums(char **);
bool is_triangular(char *);
uint32_t word_val(char *);

static uint32_t tri_nums[N_LIMIT];

