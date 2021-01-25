# Cifrul Caesar în care cheia pentru fiecare literă este
# ordinul său într-un grup Zp, cu p citit de la tastatură.
# Dacă ordinul este infinit, cheia este 0.

def indice(elt, n):
    putere = 1
    for i in range(n):
        putere = putere * elt % n
        if putere == 1:
            return i
    return 0

alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
           'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

cuv = input("Introduceți cuvîntul de criptat: ")
p = int(input("Introduceți modulul față de care lucrăm: "))

cod = []
for i in range(len(cuv)):
    cheie = indice(alfabet.index(cuv[i]), p)
    cod.append(alfabet[(alfabet.index(cuv[i]) + cheie) % 26])

print("Cuvîntul criptat este: ", end="")
for ch in cod:
    print(ch, end="")
print()
