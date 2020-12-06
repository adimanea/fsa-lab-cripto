#include<iostream>
#include<cstring>

int main() {
  char alfabet[] = {'a','b','c','d','e','f','g','h','i','j','k',
	'l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
  char plain[20], code[20];
  int k, i, pos;

  std::cout<<"Cuvîntul de criptat: ";
  std::cin>>plain;

  std::cout<<"Cheia de criptare: ";
  std::cin>>k;

  for (i = 0; i < strlen(plain); i++) {
	for (int j = 0; j < strlen(alfabet); j++)
	  if (alfabet[j] == plain[i]) {
		pos = j;
		break;
	  }
	code[i] = alfabet[(pos + k) % 26];
  }
  
  for (i = 0; i < strlen(plain); i++)
	std::cout<<code[i];
  std::cout<<std::endl;

  return 0;
}
