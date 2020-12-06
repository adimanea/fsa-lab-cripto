#include<iostream>
#include<math.h>

int main() {
  int number, mat[1000][1000], i, j, index = 2, l, c;

  std::cout<<"Introduceți marginea superioară pentru numere prime: ";
  std::cin>>number;

  for (i = 0; i < (int) sqrt(number); i++)
	for (j = 0; j < (int) sqrt(number); j++) {
	  mat[i][j] = index;
	  index++;
	}

  for (i = 0; i < (int) sqrt(number); i++)
	for (j = 0; j < (int) sqrt(number); j++) {
	  if (mat[i][j] != 0) {
		for (l = i; l < (int) sqrt(number); l++)
		  for (c = j; c < (int) sqrt(number); c++)
			if ((mat[l][c] != mat[i][j]) && (mat[l][c] % mat[i][j] == 0))
			  mat[l][c] = 0;
	  }
	}

  for (i = 0; i < (int) sqrt(number); i++) {
	for (j = 0; j < (int) sqrt(number); j++) {
	  if (mat[i][j] == 0) std::cout<<"\t";
	  else std::cout<<mat[i][j]<<"\t";
	}
	std::cout<<"\n";
  }

  return 0;
}
