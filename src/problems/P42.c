#include <stdio.h>
#include <stdlib.h>

#define T(n) n * (n + 1) / 2
#define N_LIMIT 23 
#define NUM_WORDS 2000
#define MAX_WORD 15

void fill_tri_nums(void);
void read_words(char **);
int count_tri_nums(char **);
int is_triangular(char *);
int word_val(char *);
long int binsearch(size_t, int *, size_t);
static int tri_nums[N_LIMIT];


main()
{
    int tri_word_count;
    char *words[NUM_WORDS];

    fill_tri_nums();
    read_words(words);

    printf("There are %d triangular words.\n", count_tri_nums(words));

    return 0;
}


/* fill_tri_nums: calculate triangle numbers up to N_LIMIT and store in
 * an array so we can look them up later. */
void fill_tri_nums(void)
{
    int n;

    for (n = 1; n <= N_LIMIT; n++)
        tri_nums[n - 1] = T(n);
}


/* read_words: read words from file, store in array. The words are enclosed
 * in double-quotes and seperated by commas.*/
void read_words(char **words)
{
    char c;
    int i = 0;

    *words = malloc(MAX_WORD + 1);

    while ((c = getchar()) != EOF)
        if (c == ',') {
            (*words)[i] = '\0';
            *++words = malloc(MAX_WORD + 1);
            i = 0;
        } else if (c != '\"')
            (*words)[i++] = c;
    /* Add a null pointer to terminate the array. */
    *++words = NULL;
}


/* count_tri_nums: for each word, calculate its value and check if it is
 * triangular. Return the number of triangular words. */
int count_tri_nums(char **words)
{
    int tri_word_count = 0;
 
    while (*words != NULL) 
        if (is_triangular(*words++))
            tri_word_count++;

    return tri_word_count;
}


/* is_triangular: returns 1 if a given word is triangular, 0 otherwise. */
int is_triangular(char *word)
{
    return binsearch(word_val(word), tri_nums, N_LIMIT) >= 0;
}


/* word_val: calculates the numerical value of a word, according to the sum
 * of its letter values. */
int word_val(char *word)
{
    int value = 0;
    
    while (*word != '\0')
        value += *word++ - 'A' + 1;

    return value;
}
