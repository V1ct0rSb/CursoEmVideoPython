cOposto = float(input("Comprimento do cateto oposto: "))
cAdjacente = float(input("Comprimento do cateto adjacente: "))

h = (cOposto ** 2) + (cAdjacente ** 2)
hTotal = h**(1/2)

print(f"A hipotenusa vai medir {hTotal:.2f}")