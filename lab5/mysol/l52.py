# Diffie-Hellman (calculul cheii)
import random

def prim(nr):
    for i in range(2, nr):
        if (nr % i == 0):
            return 0
    return 1

a = int(input("Cheia privată a lui Alice, a = "))
b = int(input("Cheia privată a lui Bob, b = "))

p = int(input("Numărul prim public p = "))
while (not prim(p)):
    print("Numărul introdus nu este prim. Reîncercați.")
    p = int(input("Numărul prim public p = "))

alpha = random.randint(1, p)
print(f"Am ales alpha = {alpha}")

print("Calculez cheia publică A...")
A = alpha
for i in range(1, a + 1):
    A = (alpha * A) % p
print(f"Cheia publică calculată este A = {A}.")

print("Calculez cheia publică B...")
B = alpha
for i in range(1, b + 1):
    B = (alpha * B) % p
print(f"Cheia publică calculată este B = {B}")

k_alice = B
for i in range(1, a + 1):
    k_alice = (k_alice * B) % p
print(f"Cheia comună calculată de Alice este {k_alice}")

k_bob = A
for i in range(1, b + 1):
    k_bob = (k_bob * A) % p
print(f"Cheia comună calculată de Bob este {k_bob}")
