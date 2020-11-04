#include<iostream>

int pasiCollatz(unsigned long long int start) {
  int pasi = 0;

  while (start != 1) {
	if (start % 2 == 0) start = (unsigned long long int) start / 2;
	else start = start * 3 + 1;
	pasi += 1;
  }
  return pasi;
}

int main() {
  unsigned long long int numar = 1, raspuns;
  int maxPasi = 0;

  while (numar < 10000000) {
	if (maxPasi < pasiCollatz(numar)) {
	  maxPasi = pasiCollatz(numar);
	  raspuns = numar;
	}
	numar += 1;
  }

  std::cout<<"Numărul "<<raspuns<<" necesită cei mai mulți pași, "<<maxPasi<<std::endl;

  return 0;
}

	
	
  
