/* Permutes a character array a in lexicographic order. The array must be 
 * null-terminated. Returns 0 if no more permutations exist. */
int permute(char *a, int len)
{
    int k, l;
   
    k = find_next_k(a, len);
    if (k < 0)
        return 0;
    else {
        l = find_next_l(a, len, k);
        swap_elements(a, k, l);
        reverse(a + k + 1);
    }
    return 1;
}


int find_next_k(char *a, int len)
{
    int k;

    for (k = len - 2; k >= 0; k--)
        if (a[k] <  a[k + 1])
            return k;
    return -1;
}


int find_next_l(char *a, int len, int k)
{
    int l;

    for (l = len - 1; l >= 0; l--)
        if (a[k] < a[l])
            return l;
    return -1;
}

