#include<iostream>
#include<algorithm>			// pentru funcția sort()

bool desc(int x, int y) {
  // pentru sortare descrescătoare
  return (x > y);
}

int main() {
  int num, cifreC[4], cifreD[4], i = 0, cifre[4], dif, big, small, difCopy, step = 0;

  std::cout<<"Introduceți un număr de 4 cifre, cel puțin 2 distincte: ";
  std::cin>>num;

  std::cout<<"+--------------------+\n";
  std::cout<<"| PROCEDURA KAPREKAR |\n";
  std::cout<<"+--------------------+\n";

  // pune cifrele într-un vector
  while (num != 0) {
	cifre[i++] = num % 10;
	num = (int) num / 10;
  }


  dif = 0;	  // pentru începutul buclei
  while (dif != 6174) {
	// copiază cifrele în toți vectorii
	for (int i = 0; i < 4; i++)
	  cifreC[i] = cifreD[i] = cifre[i];

	// sortează crescător și descrescător cifrele 
	std::sort(cifreC, cifreC + 4);
	std::sort(cifreD, cifreD + 4, desc);

	// formează nr mare și nr mic
	big = cifreD[3] + cifreD[2] * 10 + cifreD[1] * 100 + cifreD[0] * 1000;
	small = cifreC[3] + cifreC[2] * 10 + cifreC[1] * 100 + cifreC[0] * 1000;

	// calculează diferența și afișează rezultatul
	dif = big - small;
	std::cout<<"Pas "<<++step<<": "<<big<<" - "<<small<<" = "<<dif<<std::endl;

	difCopy = dif;
	// reia cu diferența
	i = 0;
	while (difCopy != 0) {
	  cifre[i++] = difCopy % 10;
	  difCopy = (int) difCopy / 10;
	}
  }
  
  return 0;

}
