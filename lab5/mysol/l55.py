# ElGamal
import random

def prim(nr):
    for i in range(2, nr):
        if (nr % i == 0):
            return 0
    return 1

def este_generator(g, p):
    if g not in range(2, p):
        return 0
    puteri_g = []
    gp = 1
    for i in range(p):
        gp = (gp * g) % p
        if gp not in puteri_g:
            puteri_g.append(gp)
    if (len(puteri_g) == p - 1):
        return 1
    else:
        return 0

######################################################################
    
print("Programul implementează algoritmul ElGamal.")
print("PASUL DE GENERARE A CHEILOR")

p = int(input("Introduceți un număr prim p pentru a lucra în grupul multiplicativ Zp, p = "))
while (not prim(p)):
    print("Numărul introdus nu este prim. Reîncercați.")
    p = int(input("Introduceți un număr prim p pentru a lucra în grupul multiplicativ Zp, p = "))

g = int(input(f"Introduceți un generator pentru Z{p}, g = "))
while (not este_generator(g, p)):
    print("Numărul introdus nu este generator. Reîncercați.")
    g = int(input(f"Introduceți un generator pentru Z{p}, g = "))

q = p - 1
print(f"Lucrăm în grupul multiplicativ Z{p}, cu generatorul g = {g}, e = 1 și q = {q}")

x = random.randint(1, q)
h = 1
for i in range(x):
    h = (h * g) % p

print(f"Cheia publică este PuK = (G, q, g, h) = (Z{p}, {q}, {g}, {h}).")
print(f"Cheia privată este PrK = x = {x}.")

######################################################################
print("PASUL DE CRIPTARE")

m = int(input(f"Alegeți un mesaj m, ca element al lui Z{p}*, m = "))
while m not in range(1, p):
    print("Mesajul este incorect. Reîncercați.")
    m = int(input(f"Alegeți un mesaj m, ca element al lui Z{p}*, m = "))

y = random.randint(1, q)
s = 1
for i in range(y):
    s = (s * h) % p
c1 = 1
for i in range(y):
    c1 = (c1 * g) % p
c2 = (m * s) % p

print(f"Cifrul este perechea (c1, c2) = ({c1}, {c2}).")

######################################################################
print("PASUL DE DECRIPTARE")
sDecriptare = 1
for i in range(x):
    sDecriptare = (sDecriptare * c1) % p

sDecriptareInvers = 1
for i in range(q - x):
    sDecriptareInvers = (sDecriptareInvers * c1) % p

mDecriptat = (c2 * sDecriptareInvers) % p
if (mDecriptat == m):
    print(f"Mesajul decriptat este {mDecriptat}, care coincide cu m = {m}.")
else:
    print(f"Eroare de decriptare: {mDecriptat} != {m}.")
