import random

plainString = input("Mesajul de criptat: ")

plainChars = [ch for ch in plainString]
plainAscii = [ord(ch) for ch in plainChars]
plainBin = [bin(ch) for ch in plainAscii]

randKeyDecimal = []
for i in range(len(plainChars)):
    randKeyDecimal.append(random.randint(65,126))

randKeyBin = [bin(k) for k in randKeyDecimal]

encryptedDecimal = []
for i in range(len(plainChars)):
    encryptedDecimal.append(int(randKeyBin[i], 2) ^ int(plainBin[i], 2))

encryptedChars = [chr(ed) for ed in encryptedDecimal]
encryptedString = ''
for ec in encryptedChars:
    encryptedString += str(ec)

print(encryptedString)
print()
