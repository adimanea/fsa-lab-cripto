# Programul calculează inversa unei matrice 2 x 2 cu elemente din Zn.

def cmmdc(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

def invMod(x,modul):
    for i in range(modul):
        if x * i % modul == 1:
            return x
    return 0

modul = int(input("Introduceți modulul față de care lucrăm: "))

matrice = []
print(f"Introduceți elementele matricei modulo {modul}: ")
for i in range(4):
    elt = int(input())
    matrice.append(elt)
# matricea:
# matrice[0]            matrice[1]
# matrice[2]            matrice[3]

det = (matrice[0] * matrice[3]) - (matrice[1] * matrice[2])
det = det % modul

if (cmmdc(det, modul) != 1):
    print("Matricea nu este inversabilă!")
    exit()

detInv = invMod(det, modul)

# transpusa
# matrice[0]            matrice[2]
# matrice[1]            matrice[3]
matriceT = [matrice[0], matrice[2], matrice[1], matrice[3]]

# adjuncta
# matrice[3]            -matrice[1]
# -matrice[2]           matrice[0]
matriceAdj = [matrice[3], -matrice[1], -matrice[2], matrice[0]]

# inversa
matriceInv = [(detInv * x) % modul for x in matriceAdj]
print(f"{matriceInv[0]}  {matriceInv[1]}")
print(f"{matriceInv[2]}  {matriceInv[3]}")
