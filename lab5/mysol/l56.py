# RSA
def prim(nr):
    for i in range(2, nr):
        if (nr % i == 0):
            return 0
    return 1

def cmmdc(a, b):
    while (a != b):
        if (a > b):
            a -= b
        else:
            b -= a
    return a

p = int(input("Introduceți un număr prim p = "))
while (not prim(p)):
    print("Numărul introdus nu este prim, reîncercați.")
    p = int(input("Introduceți un număr prim p = "))

q = int(input("Introduceți un al doilea număr prim q = "))
while (not prim(q)):
    print("Numărul introdus nu este prim, reîncercați.")
    q = int(input("Introduceți un al doilea număr prim q = "))

print("Calculez modulul de criptare...")
n = p * q
phi = (p - 1)*(q - 1)
print(f"Modulul de criptare este n = {n}")

e = int(input(f"Alegeți modulul de criptare, de la 3 la {phi - 1}, coprim cu {phi}, e = "))
while (cmmdc(e, phi) != 1):
    print(f"cmmdc({e}, {phi}) = {cmmdc(e,phi)} != 1. Reîncercați.")
    e = int(input(f"Alegeți modulul de criptare, de la 3 la {phi - 1}, coprim cu {phi}, e = "))

print("Calculez exponentul de decriptare...")
for i in range(1, phi):
    if ((i * e) % phi == 1):
        d = i
        break
print(f"Exponentul de decriptare este d = {d}")

print(f"Cheia publică este PuK = ({e}, {n})")
print(f"Cheia privată de decriptare este PrK = ({d}, {n})")

print("Programul poate decripta doar mesaje numerice.")
tip_mesaj = input("Cum trimiteți mesajul: (a) numeric (b) cu maximum 3 litere: ")
while (tip_mesaj.lower() not in ['a', 'b']):
    print("Opțiune invalidă. Reîncercați.")
    tip_mesaj = input("Cum trimiteți mesajul: (a) numeric (b) cu maximum 3 litere: ")

if (tip_mesaj.lower() == 'a'):
    m = int(input("Introduceți mesajul numeric m = "))
    print("Calculez mesajul criptat...")
    m = m % n
    c = m
    for i in range(1, e):
        c = (c * m) % n
    print(f"Mesajul criptat transmis de Bob este c = {c}")
    
else:
    m = input("Introduceți mesajul de maximum 3 litere m = ")
    while (len(m) > 3):
        print("Mesajul este prea lung. Reîncercați.")
        m = input("Introduceți mesajul de maximum 3 litere.")
    alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
           'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    m_zecimal = 0
    for car in m:
        m_zecimal = m_zecimal * 10 + alfabet.index(car.lower())
    print(f"Mesajul transformat numeric este m = {m_zecimal}")
    c = m_zecimal
    for i in range(1, e + 1):
        c = (c * m_zecimal) % n
    print(f"Mesajul criptat transmis de Bob este c = {c}")

print("Decriptare, varianta numerică")
print(f"Alice a primit mesajul c = {c}")
print("Decriptează...")
m_prim = 1
for i in range(1, d + 1):
    m_prim = (m_prim * c) % n
print(f"Am obținut m' = {m_prim}")
if (m_prim == m):
    print("Mesajul coincide cu m.")
else:
    print("Eroare de decriptare.")
