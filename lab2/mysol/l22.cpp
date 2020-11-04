#include<iostream>

int gcd(int a, int b) {
  while (a != b) {
	if (a > b) a -= b;
	else b -= a;
  }
  return a;
}

int main() {
  int numarator, numitor, d;

  std::cout<<"Introduceți numărătorul și numitorul fracției:"<<std::endl;
  std::cin>>numarator;
  std::cin>>numitor;

  d = gcd(numarator, numitor);
  std::cout<<"Fracția redusă este "<<((int) numarator / d)<<" / "<<((int) numitor / d)<<std::endl;

  return 0;
}
