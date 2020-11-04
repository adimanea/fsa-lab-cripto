#include<iostream>
#include<math.h>

int isPrime(unsigned long long int n) {
  for (unsigned long long int i = 2; i <= (unsigned long long int) sqrt(n); i++)
	if (n % i == 0)
	  return 0;
  return 1;
}

int main() {
  int factori[100], puteri[100], index = 0, putere = 0;
  unsigned long long int numar, i;

  std::cout<<"Introduceți numărul de descompus: ";
  std::cin>>numar;

  for (i = 0; i < 100; i++)
	factori[i] = puteri[i] = 0;

  for (i = 2; i <= numar; i++)
	if (isPrime(i) && (numar % i == 0)) {
	  putere = 0;
	  factori[index] = i;
	  while (numar % i == 0) {
		putere += 1;
		numar = (unsigned long long int) numar / i;
	  }
	  puteri[index] = putere;
	  index += 1;
	}

  std::cout<<"Descompunerea în factori primi a numărului introdus este (factor, putere):"<<std::endl;
  for (i = 0; i < index; i++)
	std::cout<<"("<<factori[i]<<", "<<puteri[i]<<")"<<std::endl;

  return 0;
}
