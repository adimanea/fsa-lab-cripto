#include<iostream>
#include<algorithm>			// pentru funcția sort()

bool desc(int x, int y) {
  // pentru sortare descrescătoare
  return (x > y);
}

int main() {
  int num, cifreC[3], cifreD[3], i = 0, cifre[3], dif, big, small, difCopy, step = 0;

  std::cout<<"Introduceți un număr de 3 cifre, cel puțin 2 distincte: ";
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
  while (dif != 495) {
	// copiază cifrele în toți vectorii
	for (int i = 0; i < 3; i++)
	  cifreC[i] = cifreD[i] = cifre[i];

	// sortează crescător și descrescător cifrele 
	std::sort(cifreC, cifreC + 3);
	std::sort(cifreD, cifreD + 3, desc);

	// formează nr mare și nr mic
	big = cifreD[2] + cifreD[1] * 10 + cifreD[0] * 100;
	small = cifreC[2] + cifreC[1] * 10 + cifreC[0] * 100;

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
