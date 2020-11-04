#include<iostream>

int gcd(int x, int y) {
  while (x != y) {
	if (x > y) x -= y;
	else y -= x;
  }
  return x;
}

int invMod(int x, int n) {
  if (x < 0) x = n + x;
  for (int i = 1; i < n; i++)
	if (i*x % n == 1)
	  return x;
}

int main() {
  int a, x, b, c, n, res, sol;

  std::cout<<"Introduceți coeficienții (a, b, c) ai ecuației a*x + b = c și modulul n"<<std::endl;
  std::cin>>a;
  std::cin>>b;
  std::cin>>c;
  std::cin>>n;

  if (c - b < 0) res = n + (c - b);
  else res = c - b;
  if (a < 0) a = n + a;

  if (gcd(a, res) != 1) {
	std::cout<<"Ecuația nu are soluții."<<std::endl;
	return 0;
  }

  sol = (res * invMod(a, n)) % n;

  std::cout<<"Soluția este x = "<<sol<<std::endl;

  return 0;
}
