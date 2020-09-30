# Introducere în criptografie: Evaluare inițială

Mai jos, cîteva întrebări simple și generale privitoare la criptografie,
matematică și C/C++. Întrebările notate cu (*) sînt considerate mai dificile.

## Criptografie
1. Cu ce se ocupă criptografia și care sînt alte domenii conexe?
2. Unde ați întîlnit (în viața reală, în filme, în cărți, în jocuri etc.)
   elemente de criptografie și care sînt acestea?
3. Dați exemplu de servicii pe care le folosiți zilnic și care (afirmă că)
   criptează datele. Ce înseamnă aceasta, în cuvintele voastre?
4. Dați exemplu de un algoritm criptografic, la ce este folosit (dacă mai
   este în uz) și cum funcționează el, în mare.
5. (*) Ce este un algoritm criptografic /simetric/?
6. (*) Ce este /hashing/-ul?
7. (*) Ce este un /nonce/?
8. Ce este procesul de /autentificare/? Dar de /autorizare/? Dați exemple
   în care cele două procese sînt diferite.
9. Putem spune că utilizarea unui lacăt cu cifru la o valiză
   este o măsură criptografică? Argumentați.
10. Cîte cifre apreciați că trebuie să aibă un număr folosit într-un algoritm
	criptografic oarecare pentru a fi sigur?
11. (*) Descrieți termenii:
	- atacul cu forță brută (brute force attack);
	- atacul man-in-the-middle (MiTM);
	- dictionary attack,
	- inginerie socială	(social engineering);
	- ethical hacking;
	- certificat digital;
	- semnătură digitală.
12. (*) Ce sînt criptomonedele?


## Matematică
1. Calculați 15 mod 3; 12 mod 8; -2 mod 5; 999 mod 2; 999 mod 3.
2. Calculați inversul lui 3 mod 7; inversul lui 5 mod 9; inversul lui 4 mod 200;
   inversul lui -3 mod 11; inversul lui -5 mod 9.

## C/C++
1. Care este diferența dintre o funcție declarată `int func(int a, int b)` și o
   funcție declarată `float func(int a, int b)`?
2. Care este diferența dintre o funcție declarată `int func(int a)` și o funcție
   declarată `void func(int a)`?
3. Ce calculează și ce afișează următoarea bucată de cod?
   ```cpp
int v[100], int m;
	
m = -9999;
for (int i = 0; i < n; i++)
if (v[i] > m)
m = v[i];
	
std::cout<<m<<endl;
	```
4. Ce calculează și ce afișează următoarea bucată de cod?
   ```cpp 
int d = 0, i = 0, v[100];
   
while (i < n) {
  if (v[i] % 3 == 0)
	d += 1;
  i += 1;
 }

std::cout<<d;
	```
5. Ce calculează și ce afișează următoarea bucată de cod?
   ```cpp
	 int guess(int a, int b) {
	   while (a != b) {
		 if (a > b) a -= b;
		 else b -= a;
	   }

	   return a;
	 }

	 int main() {
	   int m;

	   m = (24 * 40)/guess(24, 40);
	   std::cout<<guess(24, 40)<<endl;
	   std::cout<<m<<endl;

	   return 0;
	 }
   ```
6. Este greșită următoarea bucată de cod? Dacă da, corectați-o.
   Dacă nu, explicați ce calculează și ce afișează.
   ```cpp
	 #include<iostream>

	 using namespace std;

	 int invMod(int x, int m) {
	   for (int i = 0; i < m; i++)
		 if ((x * i) % m == 1)
		   return i;
	 }

	 int main() {
	   int nr = 5, mod = 11;

	   cout<<invMod(5, 11)<<endl;

	   return 42;
	 }
   ```
