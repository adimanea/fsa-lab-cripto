import random

alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
           'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

plain = input("Cuvîntul de criptat: ")
block = int(input("Lungimea blocurilor: "))

code = []
blockNumber = len(plain)//block + 1
blocks = [['a' for i in range(block)] for j in range(blockNumber)]

pos = 0

for i in range(blockNumber):
    for j in range(block):
        if (pos < len(plain)):
            blocks[i][j] = plain[pos]
            pos += 1
        else:
            blocks[i][j] = 'a'

print("Blocuri: ")
for l in blocks:
    for ch in l:
        print(ch, end="")
    print()

keys = [random.randint(0,26) for i in range(blockNumber * block)]
print("Cheile generate aleatoriu: ")
print(keys)

k = 0
for i in range(blockNumber):
    for j in range(block):
        indexOfChar = alfabet.index(blocks[i][j])
        blocks[i][j] = alfabet[(indexOfChar + keys[k]) % 26]
        k += 1

print("Cuvîntul criptat: ", end="")
for l in blocks:
    for c in l:
        print(c, end="")
print()
