# Programul rezolvă o ecuație de gradul al doilea în Zn.

def sqrtMod(x, m):
    for i in range(m):
        if i * i % m == x:
            return i
    return 0

def invMod(x, m):
    for i in range(m):
        if i * x % m == 1:
            return i
    return 0

n = int(input("Introduceți modulul față de care lucrăm: "))

print(f"Introduceți coeficienții ecuației de gradul al doilea a*x^2 + b*x + c = 0 în Z{n}:")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

delta = (b*b - 4*a*c) % n
if not sqrtMod(delta, n):
    print(f"∆ = {delta} nu este pătrat perfect în Z{n}, deci nu se poate calcula radicalul său.")
    print(f"Ecuația nu are soluții în Z{n}.")
    exit()
else:
    sqrtDelta = sqrtMod(delta, n)
    if not invMod(a, n) or not invMod(b, n) or not invMod(c, n):
        print(f"Cel puțin unul dintre coeficienți nu este inversabil în Z{n}.")
        print(f"Ecuația nu are soluții în Z{n}.")
        exit()
    else:
        x1 = (-b + sqrtDelta)*invMod(2*a, n) % n
        x2 = (-b - sqrtDelta)*invMod(2*a, n) % n
        print(f"Rădăcinile sînt: x1 = {x1}, x2 = {x2}.")        
