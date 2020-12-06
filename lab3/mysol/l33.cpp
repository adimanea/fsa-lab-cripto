#include<iostream>

int main() {
  int n;

  std::cout<<"Introduceți numărul de testat: ";
  std::cin>>n;
  
  for (int i = 2; i < n; i++) {
	int result = 1;
	for (int j = 1; j <= n-1; j++)
	  result = (result % n) * i;
	if (result % n != 1) {
	  std::cout<<n<<" nu este prim, conform testului Fermat.\n";
	  return 0;
	}
  }

  std::cout<<n<<" este prim, conform testului Fermat.\n";
  return 0;
}
