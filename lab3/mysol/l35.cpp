#include<iostream>
#include<math.h>

int power2(int n) {
  int result = 0;

  while (n % 2 == 0) {
	result++;
	n = (int) n / 2;
  }

  return result;
}

int powerModN(int base, int exponent, int modulus) {
  int result = 1;

  if (exponent == 0)
	return 1;
  
  for (int i = 1; i <= exponent; i++)
	result = (result * base) % modulus;

  return result;
}

unsigned long long int power(int b, int e) {
  unsigned long long int result = 1;

  if (e == 0)
	return 1;
  
  for (int i = 1; i <= e; i++)
	result *= b;

  return result;
}

int main() {
  int n, s, d, a, r, ad;

  std::cout<<"Introduceți numărul de testat: ";
  std::cin>>n;

  if (n % 2 == 0) {
	std::cout<<n<<" este par, deci nu poate fi prim.\n";
	return 0;
  }

  s = power2(n - 1);
  d = (int) ((n - 1) / power(2, s));

  a = 2;

  unsigned long long int x = power(a, d) % n;
  
  if ((x == 1) || (x == n - 1)) {
	std::cout<<n<<" este prim.\n";
	return 0;
  }

  for (int i = 1; i <= s - 1; i++) {
	x = x * x % n;
	if (x == 1) {
	  std::cout<<n<<" nu este prim.\n";
	  return 0;
	}
	if (x == n-1) {
	  std::cout<<n<<" este prim.\n";
	  return 0;
	}
  }

  std::cout<<n<<" nu este prim.\n";
  
  return 0;
}
