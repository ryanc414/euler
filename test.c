#include <stdio.h>
#include <math.h>

#define NUM_WORDS 2000


void read_words(char **);
int word_val(char *);
int find_max_val(char **words);

main()
{
    char *words[NUM_WORDS];
    read_words(words);

    printf("Max val: %d\n", find_max_val(words));      

    return 0;
}


int find_max_val(char **words)
{
    int val, max_val;
    while (*words != NULL) {
        if ((val = word_val(*words++)) > max_val) {
            max_val = val;
        }
    }
    return max_val;
}
