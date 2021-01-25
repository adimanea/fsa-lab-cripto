# Cifrul Caesar în care cheia pentru fiecare literă este
# radicalul indicelui său într-un grup Zp, cu p citit de la tastatură.
# Dacă ordinul este infinit, cheia este indicele însuși.

def radical(elt, mod):
    for i in range(mod):
        if i * i % mod == elt:
            return i
    return 0

alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
           'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

cuv = input("Introduceți cuvîntul de criptat: ")
m = int(input("Introduceți modulul față de care lucrăm: "))

cod = []
for ch in cuv:
    cheie = radical(alfabet.index(ch), m)
    cod.append(alfabet[(alfabet.index(ch) + cheie) % 26])

print("Cuvîntul criptat este: ", end="")
for ch in cod:
    print(ch, end="")
print()
