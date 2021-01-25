# Dacă indicele unei litere este generator pentru Zn*, cu n citit de la tastatură.
# litera se înlocuiește cu *.

def esteGenerator(g, mod):
    puteri_g = []
    putere = 1
    for i in range(1, mod):
        putere = putere * g % mod
        if putere not in puteri_g:
            puteri_g.append(putere)
    if len(puteri_g) == mod - 1:
        return 1
    return 0

alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
           'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

cuv = input("Introduceți cuvîntul de criptat: ")
m = int(input("Introduceți modulul față de care lucrăm: "))
        
for ch in cuv:
    if esteGenerator(alfabet.index(ch), m):
        print("*", end="")
    else:
        print(ch, end="")
print()
