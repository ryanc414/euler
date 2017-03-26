#include <stdio.h>

#define CIPHER_LENGTH 1000
#define SEPERATOR ','

void read_in_cipher(FILE *);

int main(int argc, char *argv[])
{
    FILE *fp;
    char cipher[CIPHER_LENGTH];

    if (argc > 1) {
        fp = fopen(argv[1], "r");
        if (fp != NULL)
            read_in_cipher(fp);
        else
            printf("Error, could not open file \"%s\".\n", argv[1]);
    } else
        printf("Error, specify filename.\n");

    return 0;    
}

void read_in_cipher(FILE *fp, char *cipher)
{
    char c;

    while ((c = getc(fp)) != EOF)
        if (c == SEPERATOR)
            cipher++;
        

}

