alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
           'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

plain = input("Cuvîntul de criptat: ")
key = int(input("Cheia de criptare: "))

code = []

for ch in plain:
    if (ch != ' ') and (ch != '.'):
        pos = alfabet.index(ch.lower())
        code.append(alfabet[(pos + key) % 26])

print("Cuvîntul criptat: ", end="")
for cr in code:
    print(cr, end="")

print()
