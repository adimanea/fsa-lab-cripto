#include<iostream>

int jacobi(int a, int p) {
  
  if (a % p == 0) return 0;

  for (int i = 1; i < p; i++)
	if ((i * i) % p == (a % p)) return 1;

  return p-1;
}

int powerModN(int base, int exponent, int modulus) {
  int result = 1;

  for (int i = 1; i <= exponent; i++)
	result = (result * base) % modulus;

  return result;
}

int main() {
  int n, b;

  std::cout<<"Introduceți numărul de testat: ";
  std::cin>>n;

  for (b = 1; b < n; b++)
	if (jacobi(b, n) != powerModN(b, (int) (n - 1)/2, n)) {
	  std::cout<<n<<" nu este prim.\n";
	  return 0;
	}

  std::cout<<n<<" este prim.\n";

  return 0;
}
  
