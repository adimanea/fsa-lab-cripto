# Programul implementează algoritmul de divizibilitate cu 11,
# folosind descompunerea în baza 10 a unui număr.

numar = int(input("Introduceți numărul a cărui divizibilitate cu 11 o testați: "))
numarCopie = numar

cifre = []
while numar > 0:
    cifre.append(numar % 10)
    numar //= 10

suma = 0
for i in range(len(cifre)):
    if i % 2 == 0:
        suma += cifre[i]
    else:
        suma -= cifre[i]                # 10 = -1 mod 11
if suma % 11 == 0:
    print(f"Numărul {numarCopie} este divizibil cu 11, cu cîtul {numarCopie // 11}.")
else:
    print(f"Numărul {numarCopie} nu este divizibil cu 11.")
