#include<iostream>

int isDivisible(unsigned long long int number) {
  
  for (int i = 1; i <= 20; i++)
	if (number % i != 0)
	  return 0;

  return 1;
}
	  

int main() {
  unsigned long long int largest = largest = 167610643200; /* 10! * 11 * 13 * 17 * 19 */
  unsigned long long int smallest = 1;

  while (smallest <= largest) {
	if (isDivisible(smallest)) {
	  std::cout<<smallest<<" is divisible by all numbers 1..20."<<std::endl;
	  break;
	}
	else smallest++;
  }

  return 0;
}

