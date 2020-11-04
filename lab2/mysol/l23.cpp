#include<iostream>

int gcd(int a, int b) {
  while (a != b) {
	if (a > b) a -= b;
	else b -= a;
  }
  return a;
}

int main() {
  int n, a[100], d, i;

  std::cout<<"Introduceți numărul de numere:"<<std::endl;
  std::cin>>n;
  std::cout<<"Acum introduceți numerele, pe rînd:"<<std::endl;
  for (i = 0; i < n; i++)
	std::cin>>a[i];

  d = a[0];

  for (i = 0; i < n; i++)
	d = gcd(d, a[i]);

  std::cout<<"cmmdc al numerelor introduse este: "<<d<<std::endl;

  return 0;
}

/* (a1, a2, a3) = ((a1, a2), a3) */
