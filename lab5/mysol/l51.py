# logaritmul discret

baza = int(input("Introduceți baza: "))
rez = int(input("Introduceți rezultatul: "))
mod = int(input("Introduceți modulul: "))

putere = baza

for i in range(1, mod + 1):
    putere = (putere * baza) % mod
    if (putere == rez):
        print(f"log_{baza}({rez}) modulo {mod} = {i + 1}")
        exit();

print("Problema nu are soluție.")
