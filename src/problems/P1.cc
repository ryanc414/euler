//multiples of 3 and 5

#include <iostream>

int Sum_ntuples(int n1, int n2)
{

  int Sum = 0;
  int N_Max = 1000;

  for (int i = 1; i < N_Max; i++)
    {
      if (i % n1 == 0)
	{
	  Sum += i;
	}
      else if (i % n2 == 0)
	{
	  Sum += i;
	}
    }

  return Sum;
}

int main()
{
  int n1 = 3;
  int n2 = 5;

  int Sum = Sum_ntuples(n1,n2);

  std::cout << Sum << "\n";

  return 0;

}
