#include<iostream>

int main() {
  unsigned long long int numar;
  
  std::cout<<"Introduceți numărul de start: ";
  std::cin>>numar;

  std::cout<<"Pașii din conjectura Collatz sînt:"<<std::endl;
  std::cout<<numar<<" -> ";

  int pasi = 0;
  
  while (numar != 1) {
	if (numar % 2 == 0) numar = (unsigned long long int) numar / 2;
	else numar = 3 * numar + 1;
	std::cout<<numar<<" -> ";
	pasi += 1;
  }

  std::cout<<"STOP.\nProcedura a durat "<<pasi<<" pași.\n";

  return 0;
}

  
