# Programul calculează ordinul de mărime al unui număr stocat pe n biți,
# cu n citit de la tastatură.
# Practic, se ia numărul de cifre a puterii lui 2 la n.

n = int(input("Introduceți numărul de biți: "))

# puterea lui 2 la n
putere = str(2**n)              # convertim în string, ca să putem lua direct lungimea

print(f"Un număr stocat pe {n} biți are {len(putere)} cifre.")
print(f"Valoarea sa maximă este {int(putere) - 1}.")
