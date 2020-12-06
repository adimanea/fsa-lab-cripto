import random

alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z']

plainString = input("Mesajul de criptat: ")
plainChars = [ch.lower() for ch in plainString if ch != ' ']

print("Caracterele de criptat:")
print(plainChars)

indices = [alfabet.index(pc) for pc in plainChars]
print("Indicii lor în alfabet:")
print(indices)

plainBin = [bin(idx) for idx in indices]
print("Codurile binare ale indicilor:")
print(plainBin)

randKeyDecimal = []
for i in range(len(plainChars)):
    randKeyDecimal.append(random.randint(0, 25))

print("Cheile de criptare (zecimale):")
print(randKeyDecimal)

randKeyBin = [bin(k) for k in randKeyDecimal]
print("Cheile de criptare (binare):")
print(randKeyBin)

encryptedDecimal = []
for i in range(len(plainChars)):
    encryptedDecimal.append((int(randKeyBin[i], 2) ^ int(plainBin[i], 2)) % 26)

print("Pozițiile criptate:")
print(encryptedDecimal)

encryptedChars = [chr(ed) for ed in encryptedDecimal]
encryptedChars = [alfabet[ed] for ed in encryptedDecimal]
encryptedString = ''
for ec in encryptedChars:
    encryptedString += str(ec)

print("Mesajul criptat:")
print(encryptedString)
print()

# XOR
# 1 0 1 1 ==> 1 + 2 + 8 = 11
# 1 1 0 1 ==> 1 + 4 + 8 = 13
# -------
# 0 1 1 0 ==> 2 + 4 = 6
