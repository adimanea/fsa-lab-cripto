# generatorii lui Zp

def prim(nr):
    for i in range(2, nr):
        if (nr % i == 0):
            return 0
    return 1

p = int(input("Introduceți un număr prim p = "))
while (not prim(p)):
    print("Numărul introdus nu este prim. Reîncercați.")
    p = int(input("Introduceți un număr prim p = "))

g = int(input(f"Introduceți un element din Z{p} pentru a-l verifica dacă este generator, g = "))
while (g not in range(1, p)):
    print(f"Numărul introdus trebuie să fie între 1 și {p - 1}. Reîncercați.")
    g = int(input(f"Introduceți un element din Z{p} pentru a-l verifica dacă este generator, g = "))

puteri_g = []
gp = 1
for i in range(p):
    gp = (gp * g) % p
    if (gp not in puteri_g):
        puteri_g.append(gp)
if (len(puteri_g) == p - 1):
    print(f"{g} este un generator pentru Z{p}.")
    print(puteri_g)
else:
    print(f"{g} nu este un generator pentru Z{p}.")
    print(f"{g} generează un subgrup de ordin {len(puteri_g)}:")
    # puteri_g.sort()
    print(puteri_g)
