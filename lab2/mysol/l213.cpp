#include<iostream>
#include<math.h>

unsigned long int nthTriang(int n) {
  int s = 0;

  if (n == 1) s = 1;
  else s = nthTriang(n-1) + n;

  return s;
}

unsigned long int countDivs(unsigned long int n) {
  int count = 2;

  for (int i = 2; i <= (int) sqrt(n); i++)
	if (n % i == 0) count++;

  return count;
}

int main() {
  unsigned long int numberOfDivs;
  int nth = 100;

  numberOfDivs = countDivs(nthTriang(nth));

  while (numberOfDivs <= 100)
	numberOfDivs = countDivs(nthTriang(nth++));
	

  printf("%lu is the %d triangular number with over 100 divs.\n", nthTriang(nth-1), nth-1);

  return 0;
}
