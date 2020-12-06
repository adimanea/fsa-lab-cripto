import random
import numpy as np

alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
           'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

plain = input("Cuvîntul de criptat: ")

plainPos = [alfabet.index(ch) for ch in plain]

print("Vectorul necriptat: ")
print(plainPos)

randMat = [[random.randint(0,26) for i in range(len(plain))]
           for j in range(len(plain))]

print("Matricea de criptare: ")
for l in randMat:
    for c in l:
        print(c, end="\t")
    print()

code = np.matmul(np.array(randMat), np.array(plainPos)).tolist()

randVect = [random.randint(0, 26) for i in range(len(plain))]
print("Vectorul de adăugat: ")
print(randVect)

codeFinal = [(code[i] + randVect[i]) for i in range(len(plain))]
codeFinal26 = [c % 26 for c in codeFinal]

print("Vectorul criptat: ")
print(codeFinal26)

codeText = [alfabet[i] for i in codeFinal26]

print("Cuvîntul criptat: ", end="")
for c in codeText:
    print(c, end="")
print()
