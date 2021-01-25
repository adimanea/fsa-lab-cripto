# Programul calculează rădăcina de ordin r a elementului x în Zn.

n = int(input("Introduceți modulul față de care lucrăm: "))
x = int(input("Introduceți elementul a cărui rădăcină vreți să o calculați: "))
r = int(input("Introduceți ordinul rădăcinii: "))

def radacinaR(elt, ordin, mod):
    for i in range(mod):
        if i**ordin % mod == elt:
            return i
    return -1

if radacinaR(x, r, n) != -1:
    print(f"Rădăcina de ordin {r} a lui {x} în Z{n} este {radacinaR(x, r, n)}, ", end="")
    print(f"deoarece {radacinaR(x, r, n)}^{r} = {x} modulo {n}.")
else:
    print(f"Rădăcina de ordin {r} a lui {x} în Z{n} nu există.")
