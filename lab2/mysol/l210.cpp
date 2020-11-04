#include<iostream>
#include<math.h>

int gcd(int a, int b) {
  while (a != b)
	if (a > b) a -= b;
	else b -= a;

  return a;
}

int isPrime(int number) {
  for (int divisor = 2; divisor <= (int) sqrt(number); divisor++)
	if (number % divisor == 0)
	  return 0;
  return 1;
}

int main() {
  int n, d, phi = 1, coprime[99999], index = 1;

  std::cout<<"Insert a number to compute Euler's totient: ";
  std::cin>>n;

  coprime[0] = 1;

  if (isPrime(n)) {
	phi = n - 1;
	for (int i = 2; i < n; i++)
	  coprime[index++] = i;
  }
  else{
	for (d = 2; d <= (int) sqrt(n); d++)
	  if (gcd(d, n) == 1) {
		coprime[index++] = d;
		phi += 1;
	  }
  }

  std::cout<<"Euler's totient for "<<n<<" is "<<phi<<std::endl;
  std::cout<<"It is given by:"<<std::endl;

  for (int i = 0; i < index; i++)
	std::cout<<coprime[i]<<" ";

  std::cout<<std::endl;

  return 1;
}
