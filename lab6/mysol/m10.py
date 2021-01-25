# Programul calculează aria triunghiului dreptunghic determinat
# de un punct dat, proiecția sa pe OX și segmentul care unește punctul cu originea.
from math import sqrt

xP = int(input("xP = "))
yP = int(input("yP = "))

# aria triunghiului dreptunghic = produsul catetelor / 2
OA = xP
PA = yP
arie = OA * PA / 2

print(f"Aria ∆OAP = {arie}")
