# Programul afișează ordinul unui element g într-un grup multiplicativ Zn*,
# cu n citit de la tastatură.

n = int(input("Introduceți modulul față de care lucrăm: "))
g = int(input(f"Introduceți elementul din Z{n}* pentru care calculăm ordinul: "))
while g not in range(1, n):
    print(f"Elementul {g} nu aparține grupului multiplicativ Z{n}. Reîncercați.")
    g = int(input(f"Introduceți elementul din Z{n} pentru care calculăm ordinul: "))

putere_g = g
ordin = 1
for i in range(2, n):
    putere_g = putere_g * g % n
    ordin += 1
    if putere_g == 1:
        print(f"ord({g}) = {ordin} în Z{n}*")
        exit()
print(f"ord({g}) = {n - 1} în Z{n}*")
