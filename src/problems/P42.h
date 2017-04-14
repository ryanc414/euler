#include <problems.h>

#define T(n) n * (n + 1) / 2
#define N_LIMIT 23
#define NUM_WORDS 2000
#define MAX_WORD 15

void fill_tri_nums(void);
void read_words(char **);
int count_tri_nums(char **);
int is_triangular(char *);
int word_val(char *);
int binsearch(int, int *, int);

static int tri_nums[N_LIMIT];

