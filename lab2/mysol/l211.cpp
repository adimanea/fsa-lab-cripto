#include<iostream>
#include<math.h>				// for pow

int isPrime(unsigned int number) {
  for (int i = 2; i <= (int) sqrt(number); i++)
	if (number % i == 0)
	  return 0;
  return 1;
}

int gcd(int a, int b) {
  if (a > b) a -= b;
  else b -= a;

  return a;
}

int main() {
  unsigned int a, n, p, phi = 0;

  std::cout<<"Insert a positive integer, a prime and another positive integer (a, p, n): ";
  std::cin>>a;
  std::cin>>p;
  std::cin>>n;

  std::cout<<"Fermat's Little Theorem: a^p = a (mod p)\n";
  std::cout<<a<<"^"<<p<<" = "<<(int) pow((int) a, (int) p)<<" = "<<((int) pow( (int) a, (int) p) % p)<<" mod "<<p<<std::endl;

  if (isPrime(n)) phi = n - 1;
  else {
	for (int i = 1; i < n; i++)
	  if (gcd(i, n) == 1) phi++;
  }

  std::cout<<"Euler's Formula: a^phi(n) = 1 (mod n)\n";
  std::cout<<a<<"^"<<phi<<" = "<<(int) pow(a, phi)<<" = "<<((int) pow(a, phi) % n)<<" mod "<<n<<std::endl;

  return 0;
}
