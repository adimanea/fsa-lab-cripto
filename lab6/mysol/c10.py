# Cifrul Caesar în care cheia pentru fiecare literă este numărul de pași
# pe care îl face algoritmul Collatz pentru indicele său.

def pasiCollatz(n):
    if n == 0 or n == 1:
        return 0 
    pasi = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
            pasi += 1
        else:
            n = 3 * n + 1
            pasi += 1
    return pasi
            

alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
           'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

cuv = input("Introduceți cuvîntul de criptat: ")
        

chei = []
for ch in cuv:
    chei.append(pasiCollatz(alfabet.index(ch)))

cod = []
for i in range(len(cuv)):
    cod.append(alfabet[(alfabet.index(cuv[i]) + chei[i]) % 26])

for c in cod:
    print(c, end="")
print()
