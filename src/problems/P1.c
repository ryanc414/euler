/* P1: Multiples of 3 and 5 */
#include <P1.h>

/* Print the sum of multiples of 3 or 5 below 1000. */
int main()
{
  printf("%d\n", sum_ntuples(A, B));

  return 0;
}


/* Sum multiples of x and y below N_MAX. */
int sum_ntuples(int x, int y)
{
    int sum = 0;
    int i;

    for (i = 1; i < N_MAX; i++) {
        if (i % x == 0 || i % y == 0) {
	        sum += i;
	    }
    }

  return sum;
}

