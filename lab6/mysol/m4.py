# Programul calculează rădăcinile unui polinom de grad p cu coeficienți din Zn.

n = int(input("Introduceți modulul față de care lucrăm: "))
grad = int(input("Introduceți gradul polinomului: "))
if grad == 0:
    print("Doar polinomul constant nul are rădăcini.")
    exit()

print("Introduceți coeficienții polinomului: ")

coef = []
for i in range(grad + 1):
    coef.append(int(input()))

print(coef)

valoare = 0
rad = []
for i in range(n):
    for j in range(grad):
        valoare += (coef[j] * i**j) % n
        valoare %= n
    if valoare == 0:
        rad.append(i)

if rad:
    print(f"Rădăcinile polinomului introdus sînt: {rad}.")
else:
    print(f"Polinomul introdus nu are rădăcini în Z{n}.")
