# Cifrul Caesar în care cheia pentru fiecare literă este
# suma indicilor cheilor rămase din cuvînt.
# Pentru ultima literă, este indicele primei litere.

alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
           'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

cuv = input("Introduceți cuvîntul de criptat: ")

cod = []
for i in range(len(cuv)):
    suma = 0
    for j in range(i + 1, len(cuv)):
        suma += alfabet.index(cuv[j])
    if i != len(cuv) - 1:       # tratăm separat ultima literă (linia 21)
        cod.append(alfabet[(alfabet.index(cuv[i]) + suma) % 26])

ultimaCheie = alfabet.index(cuv[0])
cod.append(alfabet[ultimaCheie + alfabet.index(cuv[-1:])])

print("Cuvîntul criptat este:", end=" ")
for ch in cod:
    print(ch, end="")
print()
