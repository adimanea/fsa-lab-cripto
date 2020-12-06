#include<iostream>

int main() {
  int number, v[1000000], i, index;

  std::cout<<"Introduceți marginea superioară pentru numere prime: ";
  std::cin>>number;

  for (i = 0; i < number; i++)
	v[i] = i;

  for (i = 2; i < number; i++) {
	index = i;
	while (index < number) {
	  index += i;
	  if (v[index] != 0) v[index] = 0;
	}
  }
  
  std::cout<<"Primele mai mici decît "<<number<<" sînt:\n";
  for (i = 2; i < number; i++)
	if (v[i] != 0) std::cout<<v[i]<<" ";

  std::cout<<std::endl;

  return 0;
}

	
