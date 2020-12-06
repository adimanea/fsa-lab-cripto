# generatorii lui Zp*
def prim(nr):
    for i in range(2, nr - 1):
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

p = int(input("Introduceți un număr prim p = "))

while (not prim(p)):
    print("Numărul introdus nu este prim. Reîncercați.")
    p = int(input("Introduceți un număr prim p = "))

generatori = []
for g in range(2, p):
    if (este_generator(g, p)):
        generatori.append(g)

print(f"Generatorii grupului multiplicativ Z{p}* sînt:")
print(generatori)
