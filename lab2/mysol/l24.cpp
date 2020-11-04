#include<iostream>

int gcd(int a, int b) {

  while (a != b) {
	if (a > b) a -= b;
	else b -= a;
  }

  return a;
}

int main() {
  int n, frac[100], i, prod = 1, numitorComun, s = 0, cmmdc;

  std::cout<<"Introduceți numărul de fracții:"<<std::endl;
  std::cin>>n;

  std::cout<<"Acum introduceți-le, sub forma numărător ENTER numitor:"<<std::endl;

  for (i = 0; i < 2*n; i++)
	std::cin>>frac[i];

  cmmdc = frac[1];

  for (i = 1; i < 2*n; i += 2) {
	cmmdc = gcd(cmmdc, frac[i]);
	prod *= frac[i];
  }

  numitorComun = (int) prod/cmmdc;

  std::cout<<"Numitorul comun este: "<<numitorComun<<std::endl;

  for (i = 0; i < 2*n; i += 2) {
	frac[i] *= (int) numitorComun / frac[i+1];
	s += frac[i];
  }

  std::cout<<"Suma fracțiilor este: "<<s<<" / "<<numitorComun<<std::endl;

  return 0;
}



	  
