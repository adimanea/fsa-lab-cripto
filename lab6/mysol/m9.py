# Programul afișează cîte numere prime sînt mai mici decît n și care este următorul număr prim.

from math import sqrt

def estePrim(p):
    for i in range(2, int(sqrt(p)) + 1):
        if p % i == 0:
            return 0
    return 1

n = int(input("Introduceți numărul n: "))
nCopie = n

nrPrime = 0
for i in range(2, n + 1):
    if estePrim(i):
        nrPrime += 1

while 1:
    n += 1
    if estePrim(n):
        break

print(f"Există {nrPrime} numere prime mai mici decît {nCopie}.")
print(f"Următorul număr prim după {nCopie} este {n}.")
