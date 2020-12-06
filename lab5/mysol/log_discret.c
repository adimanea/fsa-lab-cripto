#include <stdio.h>

int main() {
  int n, a, b, p;

  printf("Introduceți baza: ");
  scanf("%d", &a);
  printf("Introduceți rezultatul: ");
  scanf("%d", &b);
  printf("Introduceți modulul: ");
  scanf("%d", &n);

  p = a;
  for (int i = 1; i <= n; i++) {
	p = (p * a) % n;
	if (p == b) {
	  printf("log_%d(%d) modulo %d = %d\n", a, b, n, (i + 1));
	  return 0;
	}
  }

  printf("Problema nu are soluție.\n");
  return 0;
}
