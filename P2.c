//fibonacci sequence

#include <stdio.h>

int main()
{
  unsigned long N_max = 4e6;
  unsigned long n1 = 1;
  unsigned long n2 = 2;
  unsigned long n = n1 + n2;
  unsigned long long Sum = n2;

  while (n < N_max)
    {
      if (n % 2 == 0)     
        {	  
          Sum += n;
        }
      n1 = n2;
      n2 = n;
      n = n1 + n2;
    }

  printf("%llu\n", Sum);
  return 0;
}
