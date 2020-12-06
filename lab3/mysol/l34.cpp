#include<iostream>
#include<stdlib.h>		/* for rand() */

int main() {
  int number, random, howMany, prob = 1;

  std::cout<<"Introduceți numărul de testat: ";
  std::cin>>number;

  std::cout<<"Cîte teste aleatorii se vor face? ";
  std::cin>>howMany;

  std::cout<<"--------------------------------------------------\n";

  for (int i = 1; i <= howMany; i++) {
	random = std::rand() % number;
	std::cout<<"Testăm "<<random;
	int result = 1;
	for (int j = 1; j <= number - 1; j++)
	  result = (result % number) * random;
	if (result % number != 1) {
	  std::cout<<". Rezultat negativ.\n";
	  prob = 0;
	}
	else std::cout<<". Rezultat pozitiv.\n";
  }

  std::cout<<"--------------------------------------------------\n";
  if (prob == 1) std::cout<<number<<" este probabil prim (Fermat).\n";
  else std::cout<<number<<" nu este prim (Fermat).\n";

  return 0;
}

  
  
