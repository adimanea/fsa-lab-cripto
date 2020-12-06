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
code26 = [c % 26 for c in code]

print("Vectorul criptat: ")
print(code26)

codeText = [alfabet[i] for i in code26]

print("Cuvîntul criptat: ", end="")
for c in codeText:
    print(c, end="")
print()
