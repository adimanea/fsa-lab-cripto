# Programul calculează ecuația dreptei prin 2 puncte date.

print("Considerăm ecuația dreptei AB, cu punctele A, B introduse de la tastatură.")

xA = int(input("xA = "))
yA = int(input("yA = "))
xB = int(input("xB = "))
yB = int(input("yB = "))

if (xA == xB):
    print(f"Dreapta este verticală, de ecuație x = {xA}.")
    exit()
if (yA == yB):
    print(f"Dreapta este orizontală, de ecuație y = {yA}.")

# y = mx + n
m = round((yB - yA) / (xB - xA), 2)
n = round(yA - m * xA, 2)

print(f"Ecuația dreptei prin punctele ({xA}, {yA}) și ({xB}, {yB}) este y = {m}*x + {n}.")
