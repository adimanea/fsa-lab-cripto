import random

alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
           'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

qs = [
    "Care este mîncarea preferată? ",
    "Unde locuiți? ",
    "Unde v-ați născut? ",
    "Care este culoarea preferată? ",
    "Unde ați vrea să călătoriți? ",
    "Care este animalul preferat? ",
    "Care este filmul preferat? ",
    "Care este cartea preferată? ",
    "Care este băutura preferată? ",
]

plain = input("Cuvîntul de criptat: ")

key = []
while (len(key) < len(plain)):
    qNo = random.randint(0, len(qs) - 1)
    ans = input(qs[qNo])
    for ch in ans:
        if (ch != ' ') and (ch != '.'):
            key.append(ch)

key = [alfabet.index(k.lower()) for k in key]

print("Cheia de criptare: ")
print(key[0:len(plain)])

code = []
j = 0

for ch in plain:
    if (ch != ' ') and (ch != '.'):
        pos = alfabet.index(ch.lower())
        code.append(alfabet[(pos + key[j]) % 26])
        j += 1

print("Cuvîntul criptat: ", end="")
for cr in code:
    print(cr, end="")

print()
