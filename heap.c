#include <stdio.h>

void generate(int, char *);
void swap(char *, int, int);
void print_array(char *A);

void generate(int n, char *A)
{
    int i;
    
    if (n == 1)
        print_array(A);
    else {
        for(i = 0; ; i++) {
            generate(n - 1, A);
            if (i == (n - 1))
                break;
            if (n % 2 == 0)
                swap(A, i, n - 1);
            else
                swap(A, 0, n - 1);
        }
    }
}


void swap(char *A, int a, int b)
{
    char tmp;

    tmp = A[a];
    A[a] = A[b];
    A[b] = tmp;
}


void print_array(char *A)
{
    while (*A != '\0')
        printf("%d", *A++);
    putchar('\n');
}
            
