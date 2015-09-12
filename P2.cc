//fibonacci sequence

#include <iostream>

int main()
{

  long N_max = 4e6;
  long n1 = 1;
  long n2 = 2;
  long n = 0;

  long long Sum = n2;

  while (n < N_max)
    {

      n = n1 + n2;

      if (n > N_max)
	{
	  break;
	}
      else
	{
	  n1 = n2;
	  n2 = n;

	  if (n % 2 == 0)     
	    {	  
	      Sum += n;
	    }
	}
    }

  std::cout << Sum << "\n";

  return 0;

}
