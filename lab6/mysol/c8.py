# Dacă indicele unei litere este pătrat perfect în Z26*,
# litera se înlocuiește cu *.

def estePatrat(x):
    for i in range(26):
        if (i * i) % 26 == x:
            return 1
    return 0

alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
           'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

cuv = input("Introduceți cuvîntul de criptat: ")
        
for ch in cuv:
    if estePatrat(alfabet.index(ch)):
        print("*", end="")
    else:
        print(ch, end="")
print()
