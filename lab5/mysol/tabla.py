def prim(nr):
    for i in range(2, nr - 1):
        if (nr % i == 0):
            return 0
    return 1

p = int(input("Introduceți un număr prim p = "))
while (not prim(p)):
    print("Numărul introdus nu este prim. Reîncercați.")
    p = int(input("Introduceți un număr prim p = "))

    
print(f"Tabla puterilor pentru Z{p}* este:")

for i in range(1, p):
    print(f"{i}\t", end="")
print()

for i in range(7*p + 1):
    print("-", end="")
print()

for i in range(1, p):
    puteri = []
    putere = 1
    for j in range(1, p):
        putere = (putere * i) % p
        puteri.append(putere)
    for elt in puteri:
        print(f"{elt}\t", end="")
    print()
