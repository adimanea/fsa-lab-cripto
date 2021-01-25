alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
           'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

cuv = input("Introduceți cuvîntul de criptat: ")
bloc = int(input("Introduceți lungimea blocului: "))

nrBloc = 0
cheieBloc = 0

blocuri = len(cuv) // bloc
if bloc * blocuri == len(cuv):
    faraRest = 1
else:
    faraRest = 0

cheiBloc = []
while nrBloc < blocuri:
    cheieBloc = 0
    for i in range(nrBloc * bloc, (nrBloc + 1) * bloc):
        cheieBloc += alfabet.index(cuv[i])
    cheiBloc.append(cheieBloc % 26)
    nrBloc += 1

cod = []

print(f"Cheile de bloc sînt: {cheiBloc}")
nrBloc = 0
while nrBloc < blocuri:
    for i in range(nrBloc * bloc, (nrBloc + 1) * bloc):
        cod.append(alfabet[(cheiBloc[nrBloc] + alfabet.index(cuv[i]))% 26])
    nrBloc += 1

if not faraRest:
    cheieBlocFinal = 0
    pozitieBlocIncomplet = bloc * nrBloc
    print(f"În final, avem un bloc incomplet, de la pozițiile {pozitieBlocIncomplet} la {len(cuv) - 1}.")
    for i in range(pozitieBlocIncomplet, len(cuv)):
        cheieBlocFinal += alfabet.index(cuv[i])
    cheieBlocFinal %= 26
    print(f"Cheia pentru acest ultim bloc este {cheieBlocFinal}.")
    for i in range(pozitieBlocIncomplet, len(cuv)):
        cod.append(alfabet[(alfabet.index(cuv[i]) + cheieBlocFinal) % 26])

print("Codul rezultat este:")
for ch in cod:
    print(ch, end="")
print()
